from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from uuid import UUID, uuid4
from datetime import datetime

class Context(BaseModel):
    device: str = "arch"
    state: str = "idle"

class JarvisRequest(BaseModel):
    session_id: UUID = Field(default_factory=uuid4)
    timestamp: float = Field(default_factory=lambda: datetime.utcnow().timestamp())
    input_type: str = "text"
    content: str
    context: Context = Field(default_factory=Context)

class JarvisResponse(BaseModel):
    status: str = "success"
    mode: str = "single"
    output: str = ""
    task_id: Optional[str] = None
    steps: List[Dict[str, Any]] = []
    tool_calls: List[Dict[str, Any]] = []
    error: Optional[Dict[str, Any]] = None
