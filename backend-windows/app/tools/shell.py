import asyncio
import sys
from typing import Optional
from app.executor.sandbox import Sandbox
from app.logging.logger import logger


class ShellTool:
    def __init__(self):
        self.sandbox = Sandbox()

    async def execute(self, command: str, timeout: int = 30, workdir: Optional[str] = None) -> dict:
        sanitized = self.sandbox.sanitize_command(command)

        logger.info(f"Shell execute: {sanitized[:200]}")

        try:
            proc = await asyncio.create_subprocess_shell(
                sanitized,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=workdir,
                shell=True
            )

            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)

            result = {
                "stdout": stdout.decode("utf-8", errors="replace") if stdout else "",
                "stderr": stderr.decode("utf-8", errors="replace") if stderr else "",
                "exit_code": proc.returncode,
                "success": proc.returncode == 0
            }

            if result["stderr"]:
                logger.warning(f"Shell stderr: {result['stderr'][:500]}")

            return result

        except asyncio.TimeoutError:
            logger.error(f"Shell command timed out after {timeout}s")
            return {"stdout": "", "stderr": "Command timed out", "exit_code": -1, "success": False}
        except Exception as e:
            logger.error(f"Shell command failed: {e}")
            return {"stdout": "", "stderr": str(e), "exit_code": -1, "success": False}
