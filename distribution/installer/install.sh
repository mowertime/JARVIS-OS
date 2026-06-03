#!/bin/bash
set -euo pipefail

JARVIS_VERSION="2.0.0"
JARVIS_ROOT="/opt/jarvis"
JARVIS_USER="jarvis"
JARVIS_GROUP="jarvis"

echo "=== JARVIS OS v${JARVIS_VERSION} Installer ==="
echo ""

if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

if [ -f /etc/arch-release ]; then
    DISTRO="arch"
    PACMAN="pacman"
elif [ -f /etc/debian_version ]; then
    DISTRO="debian"
    APT="apt"
else
    echo "Unsupported distribution. Arch Linux or Debian required."
    exit 1
fi

echo "Detected: $DISTRO"

if ! id -u ${JARVIS_USER} &>/dev/null; then
    useradd -r -m -d ${JARVIS_ROOT} -s /usr/bin/nologin ${JARVIS_USER}
    echo "Created user: ${JARVIS_USER}"
fi

mkdir -p ${JARVIS_ROOT}/{backend,frontend,data,logs,etc}
mkdir -p ${JARVIS_ROOT}/backend/{app,router,executor}
mkdir -p /etc/jarvis
mkdir -p /usr/lib/jarvis

echo "Created directory structure"

if [ "$DISTRO" = "arch" ]; then
    pacman -Syu --noconfirm
    pacman -S --noconfirm python python-pip python-virtualenv alsa-utils pulseaudio espeak docker docker-compose btrfs-progs fwupd dmidecode hwinfo lshw git curl wget
elif [ "$DISTRO" = "debian" ]; then
    apt update && apt upgrade -y
    apt install -y python3 python3-pip python3-venv alsa-utils pulseaudio espeak-ng docker.io docker-compose btrfs-progs fwupd dmidecode hwinfo lshw git curl wget
fi

python3 -m venv ${JARVIS_ROOT}/venv
source ${JARVIS_ROOT}/venv/bin/activate
pip install --upgrade pip
pip install fastapi uvicorn pydantic pydantic-settings httpx aiofiles chromadb sentence-transformers numpy pyaudio openai-whisper

cp systemd/*.service /etc/systemd/system/
cp systemd/jarvis.target /etc/systemd/system/
systemctl daemon-reload

install -m 755 ../hal/jarvis-hal /usr/lib/jarvis/jarvis-hal

cat > /etc/jarvis/jarvis.conf << 'EOF'
JARVIS_HOST=0.0.0.0
JARVIS_PORT=8000
JARVIS_LOG_LEVEL=INFO
JARVIS_MEMORY_DB_PATH=/opt/jarvis/data/memory.db
JARVIS_VECTOR_STORE_PATH=/opt/jarvis/data/vectors
EOF

systemctl enable jarvis.target
systemctl enable jarvis-api.service jarvis-router.service jarvis-executor.service jarvis-memory.service jarvis-hal.service

echo ""
echo "=== JARVIS OS v${JARVIS_VERSION} Installation Complete ==="
