from typing import Dict, Any, Callable, Optional
from app.tools.shell import ShellTool
from app.tools.file_tools import FileTools
from app.tools.web_tools import WebTools
from app.tools.device import DeviceTool
from app.logging.logger import logger


class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Callable] = {}
        self._shell = ShellTool()
        self._file_tools = FileTools()
        self._web_tools = WebTools()
        self._device = DeviceTool()
        self._register_defaults()

    def _register_defaults(self):
        self.register("shell", self._shell.execute)
        self.register("file_write", self._file_tools.write)
        self.register("file_read", self._file_tools.read)
        self.register("web_search", self._web_tools.search)
        self.register("http_request", self._web_tools.http_request)
        self.register("device_action", self._device.action)

    def register(self, name: str, func: Callable):
        self._tools[name] = func
        logger.debug(f"Registered tool: {name}")

    def get(self, name: str) -> Optional[Callable]:
        return self._tools.get(name)

    def list_tools(self) -> Dict[str, str]:
        return {name: func.__doc__ or "No description" for name, func in self._tools.items()}

    async def execute(self, tool_name: str, action: str, **kwargs) -> Any:
        tool = self.get(tool_name)
        if not tool:
            raise ValueError(f"Unknown tool: {tool_name}")
        logger.info(f"Executing tool: {tool_name} - {action[:100]}")
        return await tool(action, **kwargs)
