#!/bin/bash
set -euo pipefail
echo "JARVIS OS Deploy Script v2.0.0"
echo "Usage: deploy.sh [dev|staging|prod]"
ENV=${1:-dev}
echo "Deploying to $ENV environment..."
rsync -avz --exclude '*.pyc' --exclude '__pycache__' --exclude '.git' --exclude 'venv' ../backend/ /opt/jarvis/backend/
rsync -avz --exclude '*.pyc' --exclude '__pycache__' ../frontend/ /opt/jarvis/frontend/
systemctl daemon-reload
systemctl restart jarvis-api jarvis-router jarvis-executor
echo "Deploy complete."
