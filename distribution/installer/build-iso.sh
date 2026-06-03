#!/bin/bash
set -euo pipefail

VERSION="2.0.0"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROFILE_DIR="$PROJECT_ROOT/distribution/iso-profile"
WORK_DIR="/tmp/jarvis-iso-build-$$"
OUT_DIR="${PROJECT_ROOT}/dist"

# Colors
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; CYAN='\033[0;36m'; NC='\033[0m'

echo -e "${CYAN}JARVIS OS v${VERSION} ISO Builder${NC}"

# Check prerequisites
if ! command -v mkarchiso &>/dev/null; then echo -e "${RED}Install archiso: sudo pacman -S archiso${NC}"; exit 1; fi

# Prepare
rm -rf "$WORK_DIR"
mkdir -p "$WORK_DIR/airootfs/etc/systemd/system/multi-user.target.wants"
mkdir -p "$WORK_DIR/airootfs/opt/jarvis/backend/app"
mkdir -p "$WORK_DIR/airootfs/opt/jarvis/frontend"
mkdir -p "$WORK_DIR/airootfs/opt/jarvis/shared"
mkdir -p "$WORK_DIR/airootfs/opt/jarvis/data"
mkdir -p "$WORK_DIR/airootfs/opt/jarvis/logs"
mkdir -p "$WORK_DIR/airootfs/etc/jarvis"
mkdir -p "$WORK_DIR/airootfs/usr/lib/jarvis"
mkdir -p "$WORK_DIR/airootfs/root"
mkdir -p "$OUT_DIR"

# Copy backend
cp -r "$PROJECT_ROOT/backend-windows/app/"* "$WORK_DIR/airootfs/opt/jarvis/backend/app/"
cp "$PROJECT_ROOT/backend-windows/requirements.txt" "$WORK_DIR/airootfs/opt/jarvis/backend/"
cp "$PROJECT_ROOT/backend-windows/.env.example" "$WORK_DIR/airootfs/opt/jarvis/backend/.env"

# Copy frontend
cp -r "$PROJECT_ROOT/frontend-arch/web/"* "$WORK_DIR/airootfs/opt/jarvis/frontend/web/"
cp -r "$PROJECT_ROOT/frontend-arch/voice/"* "$WORK_DIR/airootfs/opt/jarvis/frontend/voice/"
cp -r "$PROJECT_ROOT/frontend-arch/agent_client/"* "$WORK_DIR/airootfs/opt/jarvis/frontend/agent_client/"

# Copy shared
cp -r "$PROJECT_ROOT/shared/"* "$WORK_DIR/airootfs/opt/jarvis/shared/"

# Copy systemd units
for svc in jarvis-api jarvis-router jarvis-executor jarvis-memory jarvis-voice jarvis-ui jarvis-hal jarvis-driver-manager; do
  cp "$PROJECT_ROOT/distribution/systemd/${svc}.service" "$WORK_DIR/airootfs/etc/systemd/system/"
done
cp "$PROJECT_ROOT/distribution/systemd/jarvis.target" "$WORK_DIR/airootfs/etc/systemd/system/"
ln -sf ../jarvis.target "$WORK_DIR/airootfs/etc/systemd/system/multi-user.target.wants/jarvis.target"

# Copy HAL and managers
cp "$PROJECT_ROOT/distribution/hal/jarvis-hal" "$WORK_DIR/airootfs/usr/lib/jarvis/jarvis-hal" 2>/dev/null || true
cp "$PROJECT_ROOT/distribution/hal/hal.py" "$WORK_DIR/airootfs/opt/jarvis/backend/"
cp "$PROJECT_ROOT/distribution/driver-manager/driver_manager.py" "$WORK_DIR/airootfs/opt/jarvis/backend/"
cp "$PROJECT_ROOT/distribution/firmware/firmware_manager.py" "$WORK_DIR/airootfs/opt/jarvis/backend/"

# Create config
cat > "$WORK_DIR/airootfs/etc/jarvis/jarvis.conf" << 'CONFEOF'
JARVIS_HOST=0.0.0.0
JARVIS_PORT=8000
JARVIS_LOG_LEVEL=INFO
JARVIS_MEMORY_DB_PATH=/opt/jarvis/data/memory.db
CONFEOF

# Copy ISO profile
cp "$PROFILE_DIR/pacman.conf" "$WORK_DIR/"
cp "$PROFILE_DIR/profiledef.sh" "$WORK_DIR/"
cp -r "$PROFILE_DIR/efiboot" "$WORK_DIR/"
cp -r "$PROFILE_DIR/syslinux" "$WORK_DIR/"
cp -r "$PROFILE_DIR/grub" "$WORK_DIR/"
cp "$PROFILE_DIR/airootfs/root/customize_airootfs.sh" "$WORK_DIR/airootfs/root/"
chmod +x "$WORK_DIR/airootfs/root/customize_airootfs.sh"

# Build ISO
ISO_OUT="${OUT_DIR}/jarvis-os-${VERSION}-x86_64.iso"
mkarchiso -v -w "$WORK_DIR" -o "$OUT_DIR" "$WORK_DIR"

if [ -f "${OUT_DIR}/jarvis-os-${VERSION}-x86_64.iso" ]; then
    echo -e "${GREEN}ISO built: $ISO_OUT${NC}"
    echo "Write to USB: sudo dd if=$ISO_OUT of=/dev/sdX bs=4M status=progress && sync"
else
    echo -e "${RED}ISO build failed${NC}"
    exit 1
fi

rm -rf "$WORK_DIR"
