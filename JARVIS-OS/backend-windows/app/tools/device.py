import platform
import sys
import subprocess
from typing import Optional
from app.logging.logger import logger


class DeviceTool:
    async def action(self, action_type: str, **kwargs) -> dict:
        actions = {
            "system_info": self._system_info,
            "list_processes": self._list_processes,
            "network_status": self._network_status,
            "disk_usage": self._disk_usage,
            "notify": self._send_notification
        }

        handler = actions.get(action_type)
        if not handler:
            return {"success": False, "error": f"Unknown device action: {action_type}"}

        return await handler(**kwargs)

    async def _system_info(self, **kwargs) -> dict:
        return {
            "success": True,
            "platform": platform.platform(),
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "hostname": platform.node()
        }

    async def _list_processes(self, **kwargs) -> dict:
        try:
            if sys.platform == "win32":
                result = subprocess.run(["tasklist", "/FO", "CSV", "/NH"],
                                      capture_output=True, text=True, timeout=10)
                processes = []
                for line in result.stdout.strip().split("\n")[:50]:
                    parts = line.strip('"').split('","')
                    if len(parts) >= 2:
                        processes.append({"name": parts[0], "pid": parts[1]})
                return {"success": True, "processes": processes, "count": len(processes)}
            else:
                result = subprocess.run(["ps", "aux", "--sort=-%cpu"],
                                      capture_output=True, text=True, timeout=10)
                lines = result.stdout.strip().split("\n")[1:51]
                processes = []
                for line in lines:
                    parts = line.split(None, 10)
                    if len(parts) >= 11:
                        processes.append({"user": parts[0], "pid": parts[1], "cpu": parts[2],
                                        "mem": parts[3], "command": parts[10]})
                return {"success": True, "processes": processes, "count": len(processes)}
        except Exception as e:
            return {"success": False, "error": str(e)}

    async def _network_status(self, **kwargs) -> dict:
        try:
            if sys.platform == "win32":
                result = subprocess.run(["ipconfig"], capture_output=True, text=True, timeout=10)
            else:
                result = subprocess.run(["ip", "addr"], capture_output=True, text=True, timeout=10)
            return {"success": True, "output": result.stdout[:5000]}
        except Exception as e:
            return {"success": False, "error": str(e)}

    async def _disk_usage(self, **kwargs) -> dict:
        try:
            if sys.platform == "win32":
                result = subprocess.run(["wmic", "logicaldisk", "get", "size,freespace,caption"],
                                      capture_output=True, text=True, timeout=10)
            else:
                result = subprocess.run(["df", "-h"], capture_output=True, text=True, timeout=10)
            return {"success": True, "output": result.stdout[:5000]}
        except Exception as e:
            return {"success": False, "error": str(e)}

    async def _send_notification(self, title: str = "JARVIS OS", message: str = "", **kwargs) -> dict:
        try:
            if sys.platform == "win32":
                import ctypes
                ctypes.windll.user32.MessageBoxW(0, message, title, 0)
            else:
                subprocess.run(["notify-send", title, message], timeout=5)
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}
