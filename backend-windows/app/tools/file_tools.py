import aiofiles
import os
from pathlib import Path
from typing import Optional
from app.logging.logger import logger


class FileTools:
    async def write(self, path: str, content: str, mode: str = "w") -> dict:
        try:
            path_obj = Path(path)
            path_obj.parent.mkdir(parents=True, exist_ok=True)

            async with aiofiles.open(path, mode, encoding="utf-8") as f:
                await f.write(content)

            logger.info(f"File written: {path} ({len(content)} bytes)")
            return {"success": True, "path": path, "bytes": len(content)}
        except Exception as e:
            logger.error(f"File write failed: {e}")
            return {"success": False, "error": str(e)}

    async def read(self, path: str, offset: int = 0, limit: Optional[int] = None) -> dict:
        try:
            if not os.path.exists(path):
                return {"success": False, "error": f"File not found: {path}"}

            async with aiofiles.open(path, "r", encoding="utf-8") as f:
                if offset > 0:
                    await f.seek(offset)

                if limit:
                    content = await f.read(limit)
                else:
                    content = await f.read()

            return {
                "success": True,
                "content": content,
                "path": path,
                "size": len(content),
                "offset": offset
            }
        except Exception as e:
            logger.error(f"File read failed: {e}")
            return {"success": False, "error": str(e)}

    async def list_directory(self, path: str = ".") -> dict:
        try:
            items = []
            for entry in os.scandir(path):
                items.append({
                    "name": entry.name,
                    "type": "directory" if entry.is_dir() else "file",
                    "size": entry.stat().st_size if entry.is_file() else 0,
                    "modified": entry.stat().st_mtime
                })
            return {"success": True, "path": path, "items": items, "count": len(items)}
        except Exception as e:
            logger.error(f"Directory listing failed: {e}")
            return {"success": False, "error": str(e)}
