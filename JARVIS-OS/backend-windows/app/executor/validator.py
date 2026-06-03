import json
from typing import Dict, Any, List
from app.config import settings
from app.logging.logger import logger

class Validator:
    def __init__(self):
        self.valid_tools = set(settings.tool_allowlist)
        self.risk_levels = {"low": 0, "medium": 1, "high": 2}

    def validate_tool_call(self, tool_call: Dict[str, Any]) -> Dict[str, Any]:
        errors = []

        if not isinstance(tool_call, dict):
            return {"valid": False, "reason": "Tool call must be a dictionary", "tool_call": tool_call}

        tool = tool_call.get("tool")
        if not tool:
            return {"valid": False, "reason": "Missing 'tool' field", "tool_call": tool_call}

        if tool not in self.valid_tools:
            return {"valid": False, "reason": f"Tool '{tool}' not in allowlist", "tool_call": tool_call}

        action = tool_call.get("action")
        if not action:
            return {"valid": False, "reason": "Missing 'action' field", "tool_call": tool_call}

        risk = tool_call.get("risk_level", "low")
        if risk not in self.risk_levels:
            return {"valid": False, "reason": f"Invalid risk level: {risk}", "tool_call": tool_call}

        return {
            "valid": True,
            "tool_call": tool_call,
            "risk_level": risk,
            "requires_confirmation": self.risk_levels[risk] >= self.risk_levels.get("high", 2)
        }

    def validate_json(self, data: str) -> bool:
        try:
            json.loads(data)
            return True
        except json.JSONDecodeError:
            return False

    def validate_schema(self, data: Dict[str, Any], schema: Dict[str, Any]) -> bool:
        for key, expected_type in schema.items():
            if key not in data:
                logger.warning(f"Missing key in schema: {key}")
                return False
            if not isinstance(data[key], expected_type):
                logger.warning(f"Type mismatch for {key}: expected {expected_type}, got {type(data[key])}")
                return False
        return True
