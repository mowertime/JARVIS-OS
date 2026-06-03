# JARVIS OS Windows Node Setup Script
param(
    [string]$InstallDir = "C:\Program Files\JARVIS OS",
    [switch]$InstallOllama,
    [switch]$InstallModels
)

$ErrorActionPreference = "Stop"
$Version = "2.0.0"

Write-Host "=== JARVIS OS v$Version Windows Setup ===" -ForegroundColor Cyan
Write-Host ""

# Check Python
try {
    $pythonVersion = python --version
    Write-Host "Python: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python not found. Install Python 3.10+ from python.org" -ForegroundColor Red
    exit 1
}

# Create directories
Write-Host "Creating directories..." -ForegroundColor Yellow
New-Item -ItemType Directory -Path "$InstallDir\data" -Force | Out-Null
New-Item -ItemType Directory -Path "$InstallDir\logs" -Force | Out-Null

# Create virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
python -m venv "$InstallDir\venv"
& "$InstallDir\venv\Scripts\pip" install --upgrade pip

# Install dependencies
Write-Host "Installing Python dependencies..." -ForegroundColor Yellow
Copy-Item "..\backend-windows\requirements.txt" "$InstallDir\"
& "$InstallDir\venv\Scripts\pip" install -r "$InstallDir\requirements.txt"

# Create config
Write-Host "Creating configuration..." -ForegroundColor Yellow
@"
JARVIS_HOST=0.0.0.0
JARVIS_PORT=8000
JARVIS_DEBUG=false
JARVIS_MEMORY_DB_PATH=$InstallDir\data\memory.db
JARVIS_VECTOR_STORE_PATH=$InstallDir\data\vectors
JARVIS_LOG_LEVEL=INFO
JARVIS_LOG_FILE=$InstallDir\logs\jarvis.log
"@ | Out-File -FilePath "$InstallDir\.env" -Encoding UTF8

# Install Ollama if requested
if ($InstallOllama) {
    Write-Host "Installing Ollama..." -ForegroundColor Yellow
    # Ollama Windows install
    $ollamaUrl = "https://ollama.com/download/OllamaSetup.exe"
    $ollamaInstaller = "$env:TEMP\OllamaSetup.exe"
    Invoke-WebRequest -Uri $ollamaUrl -OutFile $ollamaInstaller
    Start-Process -Wait -FilePath $ollamaInstaller -ArgumentList "/S"
    
    if ($InstallModels) {
        Write-Host "Downloading AI models..." -ForegroundColor Yellow
        & "ollama" pull qwen2.5
        & "ollama" pull llama3
        & "ollama" pull deepseek-coder
    }
}

Write-Host ""
Write-Host "=== Setup Complete ===" -ForegroundColor Green
Write-Host ""
Write-Host "To start JARVIS OS:"
Write-Host "  cd $InstallDir"
Write-Host "  .\venv\Scripts\activate"
Write-Host "  python -m app.main"
Write-Host ""
Write-Host "Or register as a Windows service using NSSM."
