# JARVIS OS Deployment Guide

## Prerequisites

### Windows Node
- Python 3.10+
- Ollama (for local LLM inference)
- 16GB+ RAM recommended
- NVIDIA GPU recommended for AI workloads

### Arch Linux Node
- Arch Linux (or Debian LTS)
- Python 3.10+
- PulseAudio or ALSA (for voice)
- Microphone and speakers

## Installation

### 1. Quick Install (Arch Linux)

```bash
# Clone repository
git clone https://github.com/jarvis-os/jarvis-os.git
cd jarvis-os

# Run installer
sudo bash distribution/installer/install.sh

# Configure
sudo bash distribution/installer/configure.sh

# Start services
sudo systemctl start jarvis.target
```

### 2. Manual Setup

#### Windows Node

```bash
# Create virtual environment
cd backend-windows
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Install Ollama models
ollama pull qwen2.5
ollama pull llama3
ollama pull deepseek-coder

# Start server
python -m app.main
```

#### Arch Linux Node

```bash
cd frontend-arch
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start web UI
cd web && python -m http.server 3000

# Start voice service (optional)
python -m voice.voice_service
```

### 3. Docker Deployment

```bash
# Build backend
docker build -t jarvis-backend ./backend-windows

# Run
docker run -d \
  --name jarvis-backend \
  -p 8000:8000 \
  -v jarvis-data:/opt/jarvis/data \
  jarvis-backend
```

## Configuration

### Backend (.env)
```
JARVIS_HOST=0.0.0.0
JARVIS_PORT=8000
JARVIS_DEBUG=false
JARVIS_LOG_LEVEL=INFO
JARVIS_QWEN_ENDPOINT=http://localhost:11434/api/generate
JARVIS_LLAMA_ENDPOINT=http://localhost:11434/api/generate
JARVIS_DEEPSEEK_ENDPOINT=http://localhost:11434/api/generate
```

### Frontend (config.json)
```json
{
    "windows_node": "http://192.168.1.100:8000",
    "voice_enabled": true,
    "audio_device": "default",
    "ui_port": 3000
}
```

## Production Checklist

- [ ] Firewall configured (allow port 8000 between nodes)
- [ ] HTTPS/TLS configured for API
- [ ] Database backups scheduled
- [ ] Log rotation configured
- [ ] Resource limits set for services
- [ ] Monitoring and alerting configured
- [ ] Regular security updates enabled
