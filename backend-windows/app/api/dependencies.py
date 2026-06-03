from fastapi import Request, Depends, HTTPException
from uuid import UUID
from app.memory.working import WorkingMemory
from app.logging.logger import logger

async def get_session(request: Request) -> UUID:
    session_id = request.state.session_id if hasattr(request.state, "session_id") else None
    if not session_id:
        session_id = UUID(int=0)
    return session_id

async def validate_request(request: Request):
    if request.headers.get("content-type") != "application/json":
        raise HTTPException(status_code=415, detail="Only application/json accepted")
    return True
