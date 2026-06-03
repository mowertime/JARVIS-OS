import asyncio
from typing import Dict, Any, Callable, Optional
from app.queue.task_queue import TaskQueue, Priority
from app.logging.logger import logger

class AsyncWorker:
    def __init__(self, task_queue: TaskQueue):
        self.task_queue = task_queue
        self._handlers: Dict[str, Callable] = {}
    
    def register(self, task_type: str, handler: Callable):
        self._handlers[task_type] = handler
        self.task_queue.register_handler(task_type, handler)
    
    async def submit(self, task_type: str, payload: Dict[str, Any],
                    priority: Priority = Priority.NORMAL) -> str:
        return await self.task_queue.enqueue(task_type, payload, priority)
    
    async def submit_voice(self, task_type: str, payload: Dict[str, Any]) -> str:
        return await self.task_queue.enqueue_voice(task_type, payload)
    
    async def get_result(self, task_id: str, wait: bool = False, 
                        timeout: Optional[float] = None) -> Optional[Dict[str, Any]]:
        if wait:
            start = asyncio.get_event_loop().time()
            while True:
                result = self.task_queue.get_status(task_id)
                if result and result["status"] in ("completed", "failed"):
                    return result
                if timeout and (asyncio.get_event_loop().time() - start) > timeout:
                    return None
                await asyncio.sleep(0.1)
        return self.task_queue.get_status(task_id)
    
    def start(self):
        self.task_queue.start()
        logger.info("Async worker started")
    
    async def stop(self):
        await self.task_queue.stop()
        logger.info("Async worker stopped")

async_worker = AsyncWorker(task_queue)
