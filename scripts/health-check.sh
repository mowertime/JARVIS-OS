#!/bin/bash
set -euo pipefail

# JARVIS OS Health Check
API_URL="${1:-http://localhost:8000}"
TIMEOUT=5

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

check_endpoint() {
    local name=$1
    local url=$2
    local result=$(curl -s -o /dev/null -w "%{http_code}" --max-time $TIMEOUT $url 2>/dev/null || echo "000")
    
    if [ "$result" = "200" ]; then
        echo -e "${GREEN}???${NC} $name ($result)"
        return 0
    else
        echo -e "${RED}???${NC} $name ($result)"
        return 1
    fi
}

echo "=== JARVIS OS Health Check ==="
echo "Target: $API_URL"
echo ""

errors=0

check_endpoint "API Health" "$API_URL/v1/health" || ((errors++))

# Check services (systemd)
if command -v systemctl &>/dev/null; then
    echo ""
    echo "Service Status:"
    for service in jarvis-api jarvis-router jarvis-executor jarvis-memory jarvis-voice jarvis-ui; do
        if systemctl is-active --quiet $service 2>/dev/null; then
            echo -e "  ${GREEN}???${NC} $service"
        else
            echo -e "  ${RED}???${NC} $service"
            ((errors++))
        fi
    done
fi

# Check Ollama
echo ""
if curl -s http://localhost:11434/api/tags --max-time 2 &>/dev/null; then
    echo -e "  ${GREEN}???${NC} Ollama running"
else
    echo -e "  ${RED}???${NC} Ollama not running"
    ((errors++))
fi

# Check memory
echo ""
mem_info=$(curl -s "$API_URL/v1/health" --max-time 2 2>/dev/null)
if [ -n "$mem_info" ]; then
    echo -e "  ${GREEN}???${NC} API responds"
fi

echo ""
if [ $errors -eq 0 ]; then
    echo -e "${GREEN}All checks passed.${NC}"
else
    echo -e "${RED}$errors check(s) failed.${NC}"
fi

exit $errors
