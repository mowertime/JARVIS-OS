from typing import Dict, Any, List, Optional
from app.logging.logger import logger

class SecurityPolicy:
    def __init__(self):
        self.policies = {
            "shell": {
                "allowlist": ["ls", "dir", "cd", "pwd", "echo", "cat", "type", 
                             "find", "grep", "where", "python", "node", "npm",
                             "pip", "git", "ipconfig", "netstat", "systeminfo",
                             "tasklist", "get-childitem", "get-content", "set-content",
                             "copy-item", "move-item", "new-item", "remove-item"],
                "blocked_args": ["sudo", "su", "passwd", "chmod", "chown",
                                "mkfs", "dd", "fdisk", "mount", "umount"]
            },
            "file_write": {
                "allowed_extensions": [".txt", ".md", ".json", ".yaml", ".yml",
                                      ".py", ".js", ".ts", ".html", ".css",
                                      ".bat", ".ps1", ".sh", ".conf", ".ini"],
                "blocked_paths": ["/etc", "/boot", "/dev", "/proc", "/sys",
                                 "C:\\Windows", "C:\\System32"]
            },
            "network": {
                "blocked_ports": [list(range(0, 1024))],
                "allowed_protocols": ["http", "https"],
                "blocked_hosts": ["localhost", "127.0.0.1", "0.0.0.0",
                                 "10.", "172.", "192.168."]
            }
        }
    
    def check_policy(self, tool: str, action: str, args: Dict[str, Any]) -> Dict[str, Any]:
        policy = self.policies.get(tool, {})
        
        if not policy:
            return {"allowed": True, "reason": "No specific policy"}
        
        if tool == "shell":
            cmd = action.strip().split()[0].lower() if action.strip() else ""
            allowlist = policy.get("allowlist", [])
            if not any(cmd.startswith(a) for a in allowlist):
                return {"allowed": False, "reason": f"Command '{cmd}' not in allowlist"}
        
        violations = []
        
        return {"allowed": len(violations) == 0, "violations": violations}
    
    def risk_assessment(self, tool: str, action: str, args: Dict[str, Any]) -> str:
        high_risk_keywords = ["delete", "remove", "destroy", "format", "install",
                            "uninstall", "shutdown", "reboot", "restart"]
        medium_risk_keywords = ["write", "create", "modify", "update", "execute",
                              "run", "download", "move", "copy"]
        
        action_lower = action.lower()
        if any(kw in action_lower for kw in high_risk_keywords):
            return "high"
        if any(kw in action_lower for kw in medium_risk_keywords):
            return "medium"
        return "low"
    
    def requires_confirmation(self, risk_level: str) -> bool:
        return risk_level == "high"

security_policy = SecurityPolicy()
