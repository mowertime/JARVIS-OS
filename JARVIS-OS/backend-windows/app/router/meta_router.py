import json
import re
from typing import Dict, Any, List, Optional
from app.models.manager import ModelManager
from app.memory.semantic import SemanticMemory
from app.logging.logger import logger
from app.config import settings

class MetaRouter:
    def __init__(self):
        self.model_manager = ModelManager()

    async def route(self, content: str, context: Dict[str, Any]) -> Dict[str, Any]:
        logger.debug(f"Routing: {content[:100]}...")

        if self._is_simple_conversation(content):
            return {
                "mode": "single",
                "steps": [{
                    "id": 1,
                    "model": "llama3",
                    "instruction": content,
                    "requires_tools": False,
                    "expected_output": "string",
                    "dependencies": []
                }],
                "final_strategy": "direct",
                "risk_level": "low",
                "requires_confirmation": False
            }

        routing_prompt = self._build_routing_prompt(content, context)

        try:
            response = await self.model_manager.query_model("qwen2.5", routing_prompt)
            plan = self._parse_router_output(response)

            if plan and "mode" in plan:
                return self._validate_and_enrich(plan, content)

        except Exception as e:
            logger.warning(f"Router LLM failed: {e}, using rule-based fallback")

        return self._rule_based_fallback(content)

    def _is_simple_conversation(self, content: str) -> bool:
        greetings = ["hello", "hi", "hey", "good morning", "good evening", "how are you", "thanks", "thank you"]
        content_lower = content.lower().strip()
        return any(content_lower.startswith(g) or content_lower == g for g in greetings)

    def _build_routing_prompt(self, content: str, context: Dict[str, Any]) -> str:
        return f"""You are JARVIS Meta Router. Analyze the user request and output ONLY valid JSON.

User Request: "{content}"
Context: {json.dumps(context)}

Determine:
1. mode: "single" (conversation only, no tools), "pipeline" (multi-step with tools), or "async" (long-running)
2. steps: list of execution steps
3. final_strategy: "direct", "merge_all", or "use_last"
4. risk_level: "low", "medium", or "high"
5. requires_confirmation: boolean

Rules:
- System operations (file writes, shell commands, installs) require pipeline mode
- Code generation requires deepseek-coder model
- Pure conversation requires single mode with llama3
- Complex reasoning requires qwen2.5
- High-risk operations (deletion, system modification) require confirmation

Output ONLY valid JSON matching this schema:
{{
    "mode": "single | pipeline | async",
    "steps": [
        {{
            "id": 1,
            "model": "llama3 | qwen2.5 | deepseek-coder",
            "instruction": "normalized instruction string",
            "requires_tools": true/false,
            "expected_output": "string | json",
            "dependencies": []
        }}
    ],
    "final_strategy": "direct | merge_all | use_last",
    "risk_level": "low | medium | high",
    "requires_confirmation": false
}}"""

    def _parse_router_output(self, response: str) -> Optional[Dict[str, Any]]:
        try:
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except (json.JSONDecodeError, AttributeError) as e:
            logger.error(f"Failed to parse router output: {e}")
        return None

    def _validate_and_enrich(self, plan: Dict[str, Any], content: str) -> Dict[str, Any]:
        plan.setdefault("mode", "single")
        plan.setdefault("steps", [])
        plan.setdefault("final_strategy", "direct")
        plan.setdefault("risk_level", "low")
        plan.setdefault("requires_confirmation", False)

        valid_steps = []
        for i, step in enumerate(plan.get("steps", [])):
            step.setdefault("id", i + 1)
            step.setdefault("model", "qwen2.5")
            step.setdefault("instruction", content)
            step.setdefault("requires_tools", False)
            step.setdefault("expected_output", "string")
            step.setdefault("dependencies", [])
            valid_steps.append(step)

        if not valid_steps:
            valid_steps.append({
                "id": 1,
                "model": "qwen2.5",
                "instruction": content,
                "requires_tools": False,
                "expected_output": "string",
                "dependencies": []
            })

        plan["steps"] = valid_steps

        risk_keywords_high = ["delete", "remove", "destroy", "format", "install", "uninstall", "shutdown", "reboot"]
        risk_keywords_medium = ["write", "create", "modify", "update", "execute", "run", "download"]

        content_lower = content.lower()
        if any(kw in content_lower for kw in risk_keywords_high):
            plan["risk_level"] = "high"
            plan["requires_confirmation"] = True
        elif any(kw in content_lower for kw in risk_keywords_medium):
            if plan["risk_level"] == "low":
                plan["risk_level"] = "medium"

        if plan["risk_level"] in ("medium", "high") and plan["mode"] == "single":
            plan["mode"] = "pipeline"

        return plan

    def _rule_based_fallback(self, content: str) -> Dict[str, Any]:
        content_lower = content.lower()

        code_keywords = ["write code", "script", "function", "implement", "program", "code that"]
        if any(kw in content_lower for kw in code_keywords):
            return {
                "mode": "pipeline",
                "steps": [{
                    "id": 1,
                    "model": "deepseek-coder",
                    "instruction": content,
                    "requires_tools": True,
                    "expected_output": "code",
                    "dependencies": []
                }],
                "final_strategy": "direct",
                "risk_level": "low",
                "requires_confirmation": False
            }

        sys_keywords = ["file", "directory", "folder", "run", "execute", "install", "list", "show"]
        if any(kw in content_lower for kw in sys_keywords):
            return {
                "mode": "pipeline",
                "steps": [{
                    "id": 1,
                    "model": "qwen2.5",
                    "instruction": content,
                    "requires_tools": True,
                    "expected_output": "string",
                    "dependencies": []
                }],
                "final_strategy": "direct",
                "risk_level": "medium",
                "requires_confirmation": False
            }

        return {
            "mode": "single",
            "steps": [{
                "id": 1,
                "model": "llama3",
                "instruction": content,
                "requires_tools": False,
                "expected_output": "string",
                "dependencies": []
            }],
            "final_strategy": "direct",
            "risk_level": "low",
            "requires_confirmation": False
        }

    async def handle_ambiguous(self, content: str) -> Dict[str, Any]:
        return {
            "requires_clarification": True,
            "clarification_message": f"I need more details to process: '{content}'. Please provide more specific instructions."
        }
