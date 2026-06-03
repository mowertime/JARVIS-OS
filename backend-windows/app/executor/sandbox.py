import re
import shlex
from typing import Dict, Any, List, Optional
from app.config import settings
from app.logging.logger import logger

class Sandbox:
    def __init__(self):
        self.blocked_patterns = [
            r'\bsudo\b', r'\bsu\b', r'\bpasswd\b',
            r'rm\s+-rf\s+/', r'format\s+\w:', r'del\s+/[fqs]/[fqs]\s+',
            r'mkfs\.', r'dd\s+if=', r'>\s+/dev/',
            r'chmod\s+777', r'chown\s+root',
            r':\(\)\s*\{', r'\bwget\s+.*\|\s*bash', r'\bcurl\s+.*\|\s*bash'
        ]
        self._compiled = [re.compile(p, re.IGNORECASE) for p in self.blocked_patterns]

    def sanitize_command(self, command: str) -> str:
        if len(command) > (settings.max_command_length if hasattr(settings, 'max_command_length') else 1000):
            raise ValueError("Command exceeds maximum length")

        for pattern in self._compiled:
            if pattern.search(command):
                raise ValueError(f"Command blocked by security policy: contains prohibited pattern")

        try:
            parts = shlex.split(command)
        except Exception as e:
            raise ValueError(f"Invalid shell syntax: {e}")

        allowed_prefixes = ["dir", "ls", "cd", "pwd", "echo", "type", "find", "where",
                          "get-childitem", "get-content", "set-content", "copy-item",
                          "move-item", "remove-item", "new-item", "mkdir",
                          "python", "node", "npm", "pip", "git",
                          "ipconfig", "netstat", "systeminfo", "tasklist"]

        cmd = parts[0].lower() if parts else ""
        is_allowed = any(cmd.startswith(prefix) for prefix in allowed_prefixes)

        if not is_allowed:
            logger.warning(f"Command not in allowlist: {cmd}")

        return command

    def is_safe_path(self, path: str) -> bool:
        dangerous = ["..\\", "../", "~\\", "~/", "\\Windows\\System32\\", "%SystemRoot%"]
        return not any(d in path for d in dangerous)
