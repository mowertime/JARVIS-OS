from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional, List, Dict, Literal

from pydantic import BaseModel, Field

from .constants import (
    InputType,
    ResponseMode,
    TaskStatus,
    DeviceState,
    ToolType,
    RiskLevel,
    ErrorCode,
)


class SessionContext(BaseModel):
    device: str = Field(..., description="Device identifier")
    state: DeviceState = Field(default=DeviceState.IDLE, description="Current device state")


class JarvisRequest(BaseModel):
    session_id: UUID = Field(default_factory=uuid4, description="Unique session identifier")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Request timestamp")
    input_type: InputType = Field(..., description="Type of input (text or voice)")
    content: str = Field(..., min_length=1, max_length=100_000, description="Input content")
    context: SessionContext = Field(default_factory=lambda: SessionContext(device="default"), description="Session context")


class ErrorInfo(BaseModel):
    status: Literal["failed"] = "failed"
    error_code: ErrorCode = Field(..., description="Error code identifying failure type")
    message: str = Field(..., description="Human-readable error message")
    retryable: bool = Field(default=False, description="Whether the operation can be retried")


class ToolCall(BaseModel):
    tool: ToolType = Field(..., description="The tool to invoke")
    action: str = Field(..., min_length=1, description="Action to perform with the tool")
    args: Dict[str, object] = Field(default_factory=dict, description="Arguments for the tool action")
    risk_level: RiskLevel = Field(default=RiskLevel.LOW, description="Risk level of this tool call")
    requires_confirmation: bool = Field(default=False, description="Whether user confirmation is required")


class Step(BaseModel):
    id: str = Field(..., description="Unique step identifier")
    model: str = Field(..., description="Model assigned to this step")
    instruction: str = Field(..., min_length=1, description="Instruction for this step")
    requires_tools: bool = Field(default=False, description="Whether this step requires tool execution")
    expected_output: str = Field(default="", description="Expected output description")
    dependencies: List[str] = Field(default_factory=list, description="List of step IDs this step depends on")


class RouterOutput(BaseModel):
    mode: ResponseMode = Field(..., description="Execution mode")
    steps: List[Step] = Field(..., min_length=1, description="Ordered list of execution steps")
    final_strategy: str = Field(..., description="Final strategy description")
    risk_level: RiskLevel = Field(default=RiskLevel.LOW, description="Overall risk level")
    requires_confirmation: bool = Field(default=False, description="Whether the full plan requires confirmation")


class JarvisResponse(BaseModel):
    status: Literal["success", "partial", "failed"] = Field(..., description="Response status")
    mode: ResponseMode = Field(..., description="Execution mode used")
    output: Optional[str] = Field(default=None, description="Response output content")
    task_id: Optional[str] = Field(default=None, description="Associated task identifier")
    steps: List[Step] = Field(default_factory=list, description="Execution steps")
    tool_calls: List[ToolCall] = Field(default_factory=list, description="Tool calls made")
    error: Optional[ErrorInfo] = Field(default=None, description="Error information if failed")


class TaskState(BaseModel):
    task_id: str = Field(..., description="Unique task identifier")
    status: TaskStatus = Field(default=TaskStatus.RECEIVED, description="Current task status")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Task creation timestamp")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update timestamp")
    request: JarvisRequest = Field(..., description="Original request")
    response: Optional[JarvisResponse] = Field(default=None, description="Response if completed")
    error: Optional[ErrorInfo] = Field(default=None, description="Error if task failed")
