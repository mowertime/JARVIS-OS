import json
from typing import Optional, Any, Dict
from datetime import datetime
from app.memory.store import MemoryStore
from app.logging.logger import logger

class WorkingMemory:
    
    @staticmethod
    async def set(session_id: str, key: str, value: Any):
        try:
            cursor = await MemoryStore.execute(
                "SELECT data FROM working_memory WHERE session_id = ?",
                (session_id,)
            )
            row = await cursor.fetchone()
            
            if row:
                data = json.loads(row["data"])
            else:
                data = {}
            
            data[key] = value
            
            await MemoryStore.execute(
                """INSERT INTO working_memory (session_id, data, updated_at)
                   VALUES (?, ?, datetime('now'))
                   ON CONFLICT(session_id) DO UPDATE SET
                       data = excluded.data,
                       updated_at = datetime('now')""",
                (session_id, json.dumps(data))
            )
            await MemoryStore.commit()
        except Exception as e:
            logger.error(f"Failed to set working memory: {e}")
    
    @staticmethod
    async def get(session_id: str, key: Optional[str] = None) -> Optional[Any]:
        try:
            cursor = await MemoryStore.execute(
                "SELECT data FROM working_memory WHERE session_id = ?",
                (session_id,)
            )
            row = await cursor.fetchone()
            if row:
                data = json.loads(row["data"])
                return data.get(key) if key else data
            return None
        except Exception as e:
            logger.error(f"Failed to get working memory: {e}")
            return None
    
    @staticmethod
    async def delete(session_id: str, key: Optional[str] = None):
        try:
            if key:
                cursor = await MemoryStore.execute(
                    "SELECT data FROM working_memory WHERE session_id = ?",
                    (session_id,)
                )
                row = await cursor.fetchone()
                if row:
                    data = json.loads(row["data"])
                    data.pop(key, None)
                    await MemoryStore.execute(
                        "UPDATE working_memory SET data = ?, updated_at = datetime('now') WHERE session_id = ?",
                        (json.dumps(data), session_id)
                    )
            else:
                await MemoryStore.execute(
                    "DELETE FROM working_memory WHERE session_id = ?",
                    (session_id,)
                )
            await MemoryStore.commit()
        except Exception as e:
            logger.error(f"Failed to delete working memory: {e}")
    
    @staticmethod
    async def clear_expired(max_age_hours: int = 24):
        try:
            await MemoryStore.execute(
                "DELETE FROM working_memory WHERE updated_at < datetime('now', ?)",
                (f"-{max_age_hours} hours",)
            )
            await MemoryStore.commit()
        except Exception as e:
            logger.error(f"Failed to clear expired working memory: {e}")
