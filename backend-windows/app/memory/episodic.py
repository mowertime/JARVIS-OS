import json
from typing import Optional, List, Dict, Any
from datetime import datetime
from app.memory.store import MemoryStore
from app.logging.logger import logger

class EpisodicMemory:
    
    @staticmethod
    async def store(session_id: str, data: Dict[str, Any], event_type: str = "interaction"):
        try:
            await MemoryStore.execute(
                """INSERT INTO episodic_memory (session_id, event_type, content, metadata) 
                   VALUES (?, ?, ?, ?)""",
                (session_id, event_type, json.dumps(data), json.dumps({
                    "timestamp": datetime.utcnow().isoformat()
                }))
            )
            await MemoryStore.commit()
        except Exception as e:
            logger.error(f"Failed to store episodic memory: {e}")
    
    @staticmethod
    async def retrieve(session_id: Optional[str] = None, limit: int = 50, 
                      offset: int = 0) -> List[Dict[str, Any]]:
        try:
            if session_id:
                cursor = await MemoryStore.execute(
                    """SELECT * FROM episodic_memory WHERE session_id = ? 
                       ORDER BY timestamp DESC LIMIT ? OFFSET ?""",
                    (session_id, limit, offset)
                )
            else:
                cursor = await MemoryStore.execute(
                    """SELECT * FROM episodic_memory ORDER BY timestamp DESC LIMIT ? OFFSET ?""",
                    (limit, offset)
                )
            
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to retrieve episodic memory: {e}")
            return []
    
    @staticmethod
    async def search(query: str, limit: int = 10) -> List[Dict[str, Any]]:
        try:
            cursor = await MemoryStore.execute(
                """SELECT * FROM episodic_memory WHERE content LIKE ? 
                   ORDER BY timestamp DESC LIMIT ?""",
                (f"%{query}%", limit)
            )
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to search episodic memory: {e}")
            return []
    
    @staticmethod
    async def clear_session(session_id: str):
        try:
            await MemoryStore.execute(
                "DELETE FROM episodic_memory WHERE session_id = ?",
                (session_id,)
            )
            await MemoryStore.commit()
        except Exception as e:
            logger.error(f"Failed to clear episodic memory: {e}")
