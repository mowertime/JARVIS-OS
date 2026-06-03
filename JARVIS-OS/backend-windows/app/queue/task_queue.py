import asyncio
import uuid
import time
from typing import Dict, Any, Optional, List, Callable
from enum import Enum
from datetime import datetime
from app.logging.logger import logger

class Priority(Enum):
    CRITICAL = 0
    HIGH = 1
    NORMAL = 2
    LOW = 3

class Task:
    def __init__(self, task_type: str, payload: Dict[str, Any], 
                 priority: Priority = Priority.NORMAL, timeout: int = 300):
        self.id = str(uuid.uuid4())
        self.type = task_type
        self.payload = payload
        self.priority = priority
        self.timeout = timeout
        self.created_at = time.time()
        self.started_at: Optional[float] = None
        self.completed_at: Optional[float] = None
        self.status = "pending"
        self.result: Optional[Any] = None
        self.error: Optional[str] = None

class TaskQueue:
    def __init__(self):
        self._queue: asyncio.PriorityQueue = asyncio.PriorityQueue()
        self._active_tasks: Dict[str, Task] = {}
        self._completed_tasks: Dict[str, Task] = {}
        self._handlers: Dict[str, Callable] = {}
        self._running = False
        self._worker_task: Optional[asyncio.Task] = None
        self._max_concurrent = 5
        self._semaphore: Optional[asyncio.Semaphore] = None
    
    def start(self, max_concurrent: int = 5):
        self._max_concurrent = max_concurrent
        self._semaphore = asyncio.Semaphore(max_concurrent)
        self._running = True
        self._worker_task = asyncio.create_task(self._process_loop())
        logger.info(f"Task queue started (max_concurrent={max_concurrent})")
    
    async def stop(self):
        self._running = False
        if self._worker_task:
            self._worker_task.cancel()
            try:
                await self._worker_task
            except asyncio.CancelledError:
                pass
        logger.info("Task queue stopped")
    
    def register_handler(self, task_type: str, handler: Callable):
        self._handlers[task_type] = handler
        logger.debug(f"Registered handler for: {task_type}")
    
    async def enqueue(self, task_type: str, payload: Dict[str, Any],
                     priority: Priority = Priority.NORMAL, timeout: int = 300) -> str:
        task = Task(task_type, payload, priority, timeout)
        await self._queue.put((priority.value, time.time(), task))
        self._active_tasks[task.id] = task
        logger.debug(f"Enqueued task {task.id}: {task_type}")
        return task.id
    
    async def enqueue_voice(self, task_type: str, payload: Dict[str, Any]) -> str:
        return await self.enqueue(task_type, payload, Priority.HIGH)
    
    async def enqueue_critical(self, task_type: str, payload: Dict[str, Any]) -> str:
        return await self.enqueue(task_type, payload, Priority.CRITICAL)
    
    async def _process_loop(self):
        while self._running:
            try:
                _, _, task = await asyncio.wait_for(
                    self._queue.get(), timeout=1.0
                )
                
                if self._semaphore:
                    await self._semaphore.acquire()
                
                asyncio.create_task(self._execute_task(task))
                
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                logger.error(f"Queue processing error: {e}")
    
    async def _execute_task(self, task: Task):
        task.started_at = time.time()
        task.status = "running"
        
        handler = self._handlers.get(task.type)
        if not handler:
            task.status = "failed"
            task.error = f"No handler for task type: {task.type}"
            self._finalize_task(task)
            return
        
        try:
            result = await asyncio.wait_for(
                handler(task.payload),
                timeout=task.timeout
            )
            task.status = "completed"
            task.result = result
        except asyncio.TimeoutError:
            task.status = "failed"
            task.error = f"Task timed out after {task.timeout}s"
        except Exception as e:
            task.status = "failed"
            task.error = str(e)
            logger.error(f"Task {task.id} failed: {e}")
        
        self._finalize_task(task)
    
    def _finalize_task(self, task: Task):
        task.completed_at = time.time()
        self._active_tasks.pop(task.id, None)
        self._completed_tasks[task.id] = task
        if self._semaphore:
            self._semaphore.release()
        
        duration = task.completed_at - (task.started_at or task.created_at)
        logger.info(f"Task {task.id} {task.status} in {duration:.2f}s")
    
    def get_status(self, task_id: str) -> Optional[Dict[str, Any]]:
        task = self._active_tasks.get(task_id) or self._completed_tasks.get(task_id)
        if not task:
            return None
        return {
            "id": task.id,
            "type": task.type,
            "status": task.status,
            "priority": task.priority.name,
            "created_at": task.created_at,
            "started_at": task.started_at,
            "completed_at": task.completed_at,
            "result": task.result,
            "error": task.error
        }
    
    def get_stats(self) -> Dict[str, Any]:
        return {
            "active": len(self._active_tasks),
            "completed": len(self._completed_tasks),
            "queue_size": self._queue.qsize(),
            "max_concurrent": self._max_concurrent
        }

task_queue = TaskQueue()
