import re
import json
from typing import Dict, Any, List, Optional
from app.config import settings
from app.logging.logger import logger

class Sanitizer:
    def __init__(self):
        self.blocked_commands = [re.escape(cmd) for cmd in settings.blocked_commands]
        self._patterns = [re.compile(p, re.IGNORECASE) for p in self.blocked_commands]
        
        self.dangerous_patterns = [
            r'rm\s+-rf\s+/', r'rm\s+-rf\s+~',
            r'mkfs\.\w+', r'dd\s+if=',
            r':\(\)\s*\{', r'\|\s*bash', r'\|\s*sh\b',
            r'>\s*/dev/sd', r'chmod\s+777\s+/',
            r'wget\s+.*-O\s*-\s*\|\s*sh',
            r'curl\s+.*\|\s*sh',
            r'python\s+-c\s+["\']import\s+os',
            r'base64\s+-d', r'openssl\s+enc',
            r'perl\s+-e\s+', r'ruby\s+-e\s+'
        ]
        self._dangerous = [re.compile(p, re.IGNORECASE) for p in self.dangerous_patterns]
    
    def sanitize_shell_command(self, command: str) -> str:
        if not command or not command.strip():
            raise ValueError("Empty command")
        
        if len(command) > settings.max_command_length:
            raise ValueError(f"Command exceeds max length ({len(command)} > {settings.max_command_length})")
        
        for pattern in self._patterns:
            if pattern.search(command):
                raise ValueError("Command contains blocked operation")
        
        for pattern in self._dangerous:
            if pattern.search(command):
                raise ValueError("Command contains dangerous pattern")
        
        return command.strip()
    
    def sanitize_path(self, path: str) -> str:
        path = path.replace("\\", "/")
        blocked_patterns = [r'\.\./', r'~', r'//', r'\0']
        for pattern in blocked_patterns:
            if re.search(pattern, path):
                raise ValueError(f"Path contains forbidden pattern: {pattern}")
        
        return path
    
    def sanitize_filename(self, filename: str) -> str:
        sanitized = re.sub(r'[<>:"/\\|?*]', '_', filename)
        sanitized = sanitized.strip('. ')
        return sanitized or "unnamed"
    
    def sanitize_json_input(self, data: str) -> Optional[Dict[str, Any]]:
        try:
            return json.loads(data)
        except json.JSONDecodeError as e:
            logger.warning(f"Invalid JSON input: {e}")
            return None
    
    def contains_injection(self, text: str) -> bool:
        injection_patterns = [
            r'\$\{.*\}', r'`.*`', r'\$\(.*\)',
            r'--exec', r'--eval', r'-e\s+',
            r'\\x[0-9a-fA-F]{2}',
            r'%[0-9A-F]{2}',
            r'\bNULL\b', r'\bDROP\b', r'\bUNION\b',
            r'\bSELECT\b.*\bFROM\b',
            r'\bDELETE\b.*\bFROM\b',
            r'\bINSERT\b.*\bINTO\b'
        ]
        
        for pattern in injection_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return True
        return False

sanitizer = Sanitizer()
