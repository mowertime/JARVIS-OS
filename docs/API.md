# JARVIS OS API Documentation

## Base URL

```
http://WINDOWS_IP:8000
```

## Endpoints

### POST /v1/jarvis
Main API endpoint for processing natural language requests.

**Request:**
```json
{
    "session_id": "uuid-string",
    "timestamp": 1234567890.123,
    "input_type": "text",
    "content": "What files are in the current directory?",
    "context": {
        "device": "arch",
        "state": "active"
    }
}
```

**Response (Single Mode - Conversation):**
```json
{
    "status": "success",
    "mode": "single",
    "output": "Hello! How can I help you today?",
    "task_id": "session-uuid"
}
```

**Response (Pipeline Mode - Multi-step):**
```json
{
    "status": "success",
    "mode": "pipeline",
    "output": "Found 3 Python files: main.py, utils.py, config.py",
    "task_id": "session-uuid",
    "steps": [
        {"id": 1, "model": "qwen2.5", "instruction": "...", "requires_tools": true}
    ],
    "tool_calls": [
        {"tool": "shell", "action": "dir *.py", "risk_level": "low"}
    ]
}
```

**Response (Async Mode):**
```json
{
    "status": "partial",
    "mode": "async",
    "output": "Task started in background.",
    "task_id": "async-task-uuid"
}
```

### GET /v1/health
Health check endpoint.

**Response:**
```json
{
    "status": "healthy",
    "service": "JARVIS OS",
    "version": "2.0.0"
}
```

### GET /v1/task/{task_id}
Get async task status.

**Response:**
```json
{
    "id": "task-uuid",
    "type": "pipeline",
    "status": "completed",
    "created_at": 1234567890.123,
    "started_at": 1234567890.456,
    "completed_at": 1234567890.789,
    "result": {"final_output": "...", "tool_calls": []}
}
```

## Error Response Format

```json
{
    "status": "failed",
    "error_code": "MODEL_FAILURE",
    "message": "Model qwen2.5 failed to generate response",
    "retryable": true
}
```

## Error Codes

| Code | Description | Retryable |
|------|-------------|-----------|
| MODEL_FAILURE | LLM model error | Yes |
| TOOL_FAILURE | Tool execution error | Yes |
| NETWORK_FAILURE | Network communication error | Yes |
| ROUTER_FAILURE | Meta router failed to parse | Yes |
| VALIDATION_FAILURE | Schema validation failed | No |
