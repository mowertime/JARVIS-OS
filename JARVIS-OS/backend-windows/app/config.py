from pydantic_settings import BaseSettings
from typing import Optional, List
import os

class Settings(BaseSettings):
    app_name: str = "JARVIS OS"
    version: str = "2.0.0"
    debug: bool = False
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    cors_origins: List[str] = ["*"]
    
    # Models
    qwen_endpoint: str = "http://localhost:11434/api/generate"
    llama_endpoint: str = "http://localhost:11434/api/generate"
    deepseek_endpoint: str = "http://localhost:11434/api/generate"
    mistral_endpoint: str = "http://localhost:11434/api/generate"
    default_model: str = "qwen2.5"
    
    # Memory
    memory_db_path: str = "data/jarvis_memory.db"
    vector_store_path: str = "data/vectors"
    memory_embedding_model: str = "all-MiniLM-L6-v2"
    
    # Security
    tool_allowlist: List[str] = ["shell", "file_write", "file_read", "web_search", "http_request", "device_action"]
    blocked_commands: List[str] = ["sudo", "su", "chmod 777", "rm -rf /", "format", "del /f /s"]
    max_command_length: int = 1000
    require_confirmation_risk: str = "high"
    
    # Queue
    max_concurrent_tasks: int = 5
    task_timeout_seconds: int = 300
    
    # Logging
    log_level: str = "INFO"
    log_file: str = "logs/jarvis.log"
    
    model_config = {"env_prefix": "JARVIS_"}
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
