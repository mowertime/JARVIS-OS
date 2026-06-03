import json
from typing import Dict, Any, List
from app.models.manager import ModelManager
from app.logging.logger import logger

class Planner:
    def __init__(self):
        self.model_manager = ModelManager()

    async def decompose(self, task: str, context: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        prompt = f"""Decompose the following task into sequential steps.
Output ONLY a JSON array of steps.

Task: {task}

Each step must have: "id" (int), "action" (string), "description" (string), "dependencies" (array of int ids), "expected_output" (string)

Example:
[
  {{"id": 1, "action": "search_web", "description": "Search for latest information", "dependencies": [], "expected_output": "search results"}},
  {{"id": 2, "action": "summarize", "description": "Summarize findings", "dependencies": [1], "expected_output": "summary"}}
]"""

        try:
            response = await self.model_manager.query_model("qwen2.5", prompt)
            steps = json.loads(response)
            return steps if isinstance(steps, list) else []
        except Exception as e:
            logger.error(f"Planning failed: {e}")
            return [{
                "id": 1,
                "action": "process",
                "description": task,
                "dependencies": [],
                "expected_output": "completed"
            }]
