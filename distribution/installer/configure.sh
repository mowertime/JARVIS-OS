#!/bin/bash
set -euo pipefail
echo "JARVIS OS Configuration Script"
if [ ! -f /etc/jarvis/jarvis.conf ]; then
    cp ../jarvis.conf.example /etc/jarvis/jarvis.conf 2>/dev/null || cat > /etc/jarvis/jarvis.conf << 'EOF'
JARVIS_HOST=0.0.0.0
JARVIS_PORT=8000
JARVIS_LOG_LEVEL=INFO
JARVIS_MEMORY_DB_PATH=/opt/jarvis/data/memory.db
JARVIS_VECTOR_STORE_PATH=/opt/jarvis/data/vectors
EOF
fi
echo "Configuration ready at /etc/jarvis/jarvis.conf"
