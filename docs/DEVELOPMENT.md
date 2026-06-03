# JARVIS OS Development Guide

## Project Structure

```
JARVIS-OS/
├── backend-windows/       # Windows Control Node
│   └── app/
│       ├── api/          # FastAPI routes and schemas
│       ├── router/       # Meta Router and Planner
│       ├── executor/     # Execution Engine and Sandbox
│       ├── tools/        # Tool Registry and implementations
│       ├── models/       # LLM providers and Manager
│       ├── memory/       # Episodic, Semantic, Working memory
│       ├── queue/        # Task Queue and Async Workers
│       ├── security/     # Sanitizer and Security Policies
│       └── logging/      # Logging configuration
├── frontend-arch/        # Arch Linux Interface Node
│   ├── web/             # Web UI (HTML/CSS/JS)
│   ├── voice/           # Voice services (wake word, STT, TTS)
│   └── agent_client/    # Agent communication client
├── shared/               # Shared schemas and protocols
├── distribution/         # OS distribution files
│   ├── systemd/         # systemd service units
│   ├── installer/       # Installation scripts
│   ├── hal/             # Hardware Abstraction Layer
│   ├── driver-manager/  # Driver management system
│   └── firmware/        # Firmware management
├── docs/                 # Documentation
└── scripts/             # Utility scripts
```

## Development Setup

```bash
# Backend (Windows)
cd backend-windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m app.main

# Frontend (Arch)
cd frontend-arch
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Adding New Tools

1. Create tool implementation in `backend-windows/app/tools/`
2. Register in `app/tools/registry.py`
3. Add to tool allowlist in `app/config.py`
4. Add security policy in `app/security/policy.py`

## Adding New Models

1. Add provider in `backend-windows/app/models/providers.py`
2. Register in `backend-windows/app/models/manager.py`
3. Add configuration in `backend-windows/app/config.py`
4. Add routing rules in `backend-windows/app/router/meta_router.py`

## Testing

```bash
# Run backend tests
cd backend-windows
pytest tests/

# Manual API test
curl -X POST http://localhost:8000/v1/jarvis \
  -H "Content-Type: application/json" \
  -d '{"content": "Hello", "input_type": "text"}'
```

## Coding Standards

- Python: PEP 8, type hints, async/await patterns
- JavaScript: ES6+, async/await, modular design
- Shell: POSIX-compliant, error handling
- systemd: Follow freedesktop.org specification
- All services must implement proper logging
- Error states must be handled gracefully
