import json
from typing import Optional, Any, List, Dict
from datetime import datetime
from app.memory.store import MemoryStore
from app.logging.logger import logger

class SemanticMemory:
    
    @staticmethod
    async def store(key: str, value: Any, category: str = "general", confidence: float = 1.0):
        try:
            await MemoryStore.execute(
                """INSERT INTO semantic_memory (key, value, category, confidence, updated_at)
                   VALUES (?, ?, ?, ?, datetime('now'))
                   ON CONFLICT(key) DO UPDATE SET 
                       value = excluded.value,
                       category = excluded.category,
                       confidence = excluded.confidence,
                       updated_at = datetime('now')""",
                (key, json.dumps(value) if not isinstance(value, str) else value, 
                 category, confidence)
            )
            await MemoryStore.commit()
        except Exception as e:
            logger.error(f"Failed to store semantic memory: {e}")
    
    @staticmethod
    async def retrieve(key: str) -> Optional[Any]:
        try:
            cursor = await MemoryStore.execute(
                "SELECT * FROM semantic_memory WHERE key = ?",
                (key,)
            )
            row = await cursor.fetchone()
            if row:
                value = row["value"]
                try:
                    return json.loads(value)
                except (json.JSONDecodeError, TypeError):
                    return value
            return None
        except Exception as e:
            logger.error(f"Failed to retrieve semantic memory: {e}")
            return None
    
    @staticmethod
    async def search(category: Optional[str] = None, query: Optional[str] = None, 
                    limit: int = 20) -> List[Dict[str, Any]]:
        try:
            if category and query:
                cursor = await MemoryStore.execute(
                    """SELECT * FROM semantic_memory 
                       WHERE category = ? AND (key LIKE ? OR value LIKE ?)
                       ORDER BY confidence DESC, updated_at DESC LIMIT ?""",
                    (category, f"%{query}%", f"%{query}%", limit)
                )
            elif category:
                cursor = await MemoryStore.execute(
                    """SELECT * FROM semantic_memory WHERE category = ?
                       ORDER BY confidence DESC, updated_at DESC LIMIT ?""",
                    (category, limit)
                )
            elif query:
                cursor = await MemoryStore.execute(
                    """SELECT * FROM semantic_memory 
                       WHERE key LIKE ? OR value LIKE ?
                       ORDER BY confidence DESC, updated_at DESC LIMIT ?""",
                    (f"%{query}%", f"%{query}%", limit)
                )
            else:
                cursor = await MemoryStore.execute(
                    "SELECT * FROM semantic_memory ORDER BY updated_at DESC LIMIT ?",
                    (limit,)
                )
            
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to search semantic memory: {e}")
            return []
    
    @staticmethod
    async def delete(key: str):
        try:
            await MemoryStore.execute(
                "DELETE FROM semantic_memory WHERE key = ?",
                (key,)
            )
            await MemoryStore.commit()
        except Exception as e:
            logger.error(f"Failed to delete semantic memory: {e}")
    
    @staticmethod
    async def get_preferences() -> Dict[str, Any]:
        rows = await SemanticMemory.search(category="preference")
        prefs = {}
        for row in rows:
            try:
                prefs[row["key"]] = json.loads(row["value"])
            except:
                prefs[row["key"]] = row["value"]
        return prefs
