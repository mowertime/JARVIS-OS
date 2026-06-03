import asyncio
import uuid
import json
import re
from typing import Dict, Any, List, Optional
from datetime import datetime
from app.executor.sandbox import Sandbox
from app.executor.validator import Validator
from app.tools.registry import ToolRegistry
from app.models.manager import ModelManager
from app.memory.episodic import EpisodicMemory
from app.logging.logger import logger
from shared.constants import RETRY_LIMIT

class ExecutionEngine:
    def __init__(self):
        self.sandbox = Sandbox()
        self.validator = Validator()
        self.tool_registry = ToolRegistry()
        self.model_manager = ModelManager()
        self._tasks: Dict[str, Dict[str, Any]] = {}
        self._lock = asyncio.Lock()

    async def execute_pipeline(self, steps: List[Dict[str, Any]], session_id: str = None) -> Dict[str, Any]:
        results = {}
        tool_calls = []
        step_outputs = []

        for step in steps:
            step_id = step.get("id", 1)
            model = step.get("model", "qwen2.5")
            instruction = step.get("instruction", "")
            requires_tools = step.get("requires_tools", False)
            dependencies = step.get("dependencies", [])

            for dep_id in dependencies:
                if dep_id in step_outputs:
                    instruction = instruction.replace(f"{{output_{dep_id}}}", str(step_outputs[dep_id]))

            logger.info(f"Executing step {step_id}: model={model}, tools={requires_tools}")

            try:
                if requires_tools:
                    tool_plan = await self._generate_tool_plan(instruction, model)

                    for tool_call in tool_plan:
                        validated = self.validator.validate_tool_call(tool_call)
                        if not validated.get("valid"):
                            logger.warning(f"Invalid tool call: {validated.get('reason')}")
                            continue

                        result = await self._execute_tool(validated["tool_call"])
                        tool_calls.append(validated["tool_call"])
                        results[step_id] = result
                else:
                    response = await self.model_manager.generate_response(model, instruction)
                    results[step_id] = response

                step_outputs.append(step_id)

            except Exception as e:
                logger.error(f"Step {step_id} failed: {e}")
                error_info = {
                    "step_id": step_id,
                    "error": str(e),
                    "retryable": True
                }

                for attempt in range(RETRY_LIMIT):
                    logger.info(f"Retrying step {step_id}, attempt {attempt + 1}")
                    try:
                        response = await self.model_manager.generate_response(model, f"Retry: {instruction}")
                        results[step_id] = response
                        error_info = None
                        break
                    except Exception as retry_e:
                        logger.error(f"Retry {attempt + 1} failed: {retry_e}")

                if error_info:
                    return {
                        "final_output": f"Pipeline failed at step {step_id}",
                        "tool_calls": tool_calls,
                        "error": error_info
                    }

        final_output = await self._generate_final_output(results, steps)

        await EpisodicMemory.store(session_id, {
            "steps": steps,
            "results": results,
            "tool_calls": tool_calls,
            "final_output": final_output
        })

        return {
            "final_output": final_output,
            "tool_calls": tool_calls,
            "error": None
        }

    async def _generate_tool_plan(self, instruction: str, model: str) -> List[Dict[str, Any]]:
        prompt = f"""Generate tool calls for: {instruction}
Output JSON array of {{"tool": "shell|file_write|file_read|web_search|http_request|device_action", "action": "string", "args": {{}}, "risk_level": "low|medium|high"}}"""

        response = await self.model_manager.query_model(model, prompt)
        try:
            json_match = re.search(r'\[.*\]', response, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"tool": "shell", "action": instruction, "args": {}, "risk_level": "medium"}]

    async def _execute_tool(self, tool_call: Dict[str, Any]) -> Any:
        tool_name = tool_call.get("tool", "")
        action = tool_call.get("action", "")
        args = tool_call.get("args", {})

        tool_func = self.tool_registry.get(tool_name)
        if not tool_func:
            raise ValueError(f"Unknown tool: {tool_name}")

        return await tool_func(action, **args)

    async def _generate_final_output(self, results: Dict[int, Any], steps: List[Dict[str, Any]]) -> str:
        strategy = steps[-1].get("final_strategy", "direct") if steps else "direct"

        if strategy == "direct":
            last_step = max(results.keys()) if results else 0
            return str(results.get(last_step, ""))
        elif strategy == "merge_all":
            return "\n".join(str(v) for v in results.values())
        elif strategy == "use_last":
            last_step = max(results.keys()) if results else 0
            return str(results.get(last_step, ""))
        return str(list(results.values())[-1]) if results else ""

    async def start_async_task(self, steps: List[Dict[str, Any]], session_id: str = None) -> str:
        task_id = str(uuid.uuid4())
        task_info = {
            "task_id": task_id,
            "session_id": session_id,
            "status": "RECEIVED",
            "steps": steps,
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat(),
            "result": None
        }

        async with self._lock:
            self._tasks[task_id] = task_info

        asyncio.create_task(self._run_async_task(task_id, steps, session_id))

        return task_id

    async def _run_async_task(self, task_id: str, steps: List[Dict[str, Any]], session_id: str = None):
        async with self._lock:
            self._tasks[task_id]["status"] = "EXECUTING"
            self._tasks[task_id]["updated_at"] = datetime.utcnow().isoformat()

        try:
            result = await self.execute_pipeline(steps, session_id)
            async with self._lock:
                self._tasks[task_id]["status"] = "COMPLETED" if not result.get("error") else "FAILED"
                self._tasks[task_id]["result"] = result
                self._tasks[task_id]["updated_at"] = datetime.utcnow().isoformat()
        except Exception as e:
            async with self._lock:
                self._tasks[task_id]["status"] = "FAILED"
                self._tasks[task_id]["result"] = {"error": str(e)}
                self._tasks[task_id]["updated_at"] = datetime.utcnow().isoformat()

    async def get_task_status(self, task_id: str) -> Optional[Dict[str, Any]]:
        async with self._lock:
            return self._tasks.get(task_id)
