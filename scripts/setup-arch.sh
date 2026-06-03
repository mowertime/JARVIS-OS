#!/bin/bash
set -euo pipefail

echo "=== JARVIS OS Arch Linux Setup ==="

# Install dependencies
echo "Installing system packages..."
sudo pacman -Syu --noconfirm
sudo pacman -S --noconfirm \
    python python-pip python-virtualenv \
    alsa-utils pulseaudio espeak \
    git curl wget \
    fwupd dmidecode hwinfo lshw

# Setup frontend
echo "Setting up frontend..."
cd frontend-arch
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create data directories
sudo mkdir -p /opt/jarvis/{data,logs}
sudo chown -R $USER:$USER /opt/jarvis

# Create config
cat > config.json << EOF
{
    "windows_node": "http://localhost:8000",
    "voice_enabled": false,
    "audio_device": "default",
    "ui_port": 3000
}
EOF

echo ""
echo "=== Arch Linux Setup Complete ==="
echo ""
echo "Start web UI:  cd web && python -m http.server 3000"
echo "Start voice:   python -m voice.voice_service"
echo "Test backend:  curl http://localhost:8000/v1/health"
