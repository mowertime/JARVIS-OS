from fastapi import APIRouter, Depends, HTTPException
from app.api.schemas import JarvisRequest, JarvisResponse
from app.api.dependencies import get_session, validate_request
from app.router.meta_router import MetaRouter
from app.executor.engine import ExecutionEngine
from app.memory.working import WorkingMemory
from app.models.manager import ModelManager
from app.logging.logger import logger
from uuid import UUID
import traceback

router = APIRouter()
meta_router = MetaRouter()
execution_engine = ExecutionEngine()
model_manager = ModelManager()

@router.post("/jarvis", response_model=JarvisResponse)
async def process_jarvis_request(
    request: JarvisRequest,
    session_id: UUID = Depends(get_session),
    _: bool = Depends(validate_request)
):
    logger.info(f"Request [{request.session_id}] type={request.input_type} len={len(request.content)}")
    
    try:
        # Store in working memory
        await WorkingMemory.set(session_id, "current_request", request.model_dump())
        
        # Route the request
        router_output = await meta_router.route(request.content, request.context.model_dump())
        
        # Check for clarification needed
        if router_output.get("requires_clarification"):
            return JarvisResponse(
                status="partial",
                mode="single",
                output=router_output.get("clarification_message", "Please clarify your request."),
                task_id=str(request.session_id)
            )
        
        # Execute based on mode
        if router_output["mode"] == "single":
            result = await model_manager.generate_response(
                router_output["steps"][0]["model"],
                router_output["steps"][0]["instruction"]
            )
            return JarvisResponse(
                status="success",
                mode="single",
                output=result,
                task_id=str(request.session_id),
                steps=router_output["steps"]
            )
        
        elif router_output["mode"] == "pipeline":
            execution_result = await execution_engine.execute_pipeline(
                router_output["steps"],
                session_id=str(request.session_id)
            )
            return JarvisResponse(
                status="success" if not execution_result.get("error") else "failed",
                mode="pipeline",
                output=execution_result.get("final_output", ""),
                task_id=str(request.session_id),
                steps=router_output["steps"],
                tool_calls=execution_result.get("tool_calls", []),
                error=execution_result.get("error")
            )
        
        elif router_output["mode"] == "async":
            task_id = await execution_engine.start_async_task(
                router_output["steps"],
                session_id=str(request.session_id)
            )
            return JarvisResponse(
                status="partial",
                mode="async",
                output="Task started in background.",
                task_id=task_id,
                steps=router_output["steps"]
            )
        
    except Exception as e:
        logger.error(f"Request failed: {str(e)}\n{traceback.format_exc()}")
        return JarvisResponse(
            status="failed",
            mode="single",
            output="An error occurred processing your request.",
            task_id=str(request.session_id),
            error={"error_code": "INTERNAL_ERROR", "message": str(e), "retryable": True}
        )

@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "JARVIS OS", "version": "2.0.0"}

@router.get("/task/{task_id}")
async def get_task_status(task_id: str):
    result = await execution_engine.get_task_status(task_id)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return result
