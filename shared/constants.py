from enum import Enum


class ErrorCode(str, Enum):
    MODEL_FAILURE = "model_failure"
    TOOL_FAILURE = "tool_failure"
    NETWORK_FAILURE = "network_failure"
    ROUTER_FAILURE = "router_failure"
    VALIDATION_FAILURE = "validation_failure"


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TaskStatus(str, Enum):
    RECEIVED = "received"
    ROUTED = "routed"
    PLANNED = "planned"
    EXECUTING = "executing"
    WAITING = "waiting"
    COMPLETED = "completed"
    FAILED = "failed"


class InputType(str, Enum):
    TEXT = "text"
    VOICE = "voice"


class ResponseMode(str, Enum):
    SINGLE = "single"
    PIPELINE = "pipeline"
    ASYNC = "async"


class DeviceState(str, Enum):
    IDLE = "idle"
    ACTIVE = "active"
    SPEAKING = "speaking"


class ToolType(str, Enum):
    SHELL = "shell"
    FILE_WRITE = "file_write"
    FILE_READ = "file_read"
    WEB_SEARCH = "web_search"
    HTTP_REQUEST = "http_request"
    DEVICE_ACTION = "device_action"


class ModelType(str, Enum):
    QWEN2_5 = "qwen2.5"
    LLAMA3 = "llama3"
    DEEPSEEK_CODER = "deepseek-coder"
    MISTRAL7B = "mistral7b"


DEFAULT_WINDOWS_PORT = 8000
RETRY_LIMIT = 2
WAKE_WORD = "hey jarvis"
WAKE_RESPONSE = "Go ahead, sir."

Qwen2_5 = "qwen2.5"
Llama3 = "llama3"
DeepSeekCoder = "deepseek-coder"
Mistral7B = "mistral7b"
