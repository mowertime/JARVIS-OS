import httpx
import json
from typing import Optional, Dict, Any
from uuid import uuid4
from datetime import datetime
import logging

logger = logging.getLogger("jarvis.agent.client")

class JarvisAgentClient:
    def __init__(self, host: str = "http://localhost:8000"):
        self.host = host
        self.session_id = str(uuid4())
        self._client = httpx.AsyncClient(timeout=60.0)
    
    async def send(self, content: str, input_type: str = "text") -> Dict[str, Any]:
        payload = {
            "session_id": self.session_id,
            "timestamp": datetime.utcnow().timestamp(),
            "input_type": input_type,
            "content": content,
            "context": {
                "device": "arch",
                "state": "active"
            }
        }
        
        logger.info(f"Sending request: {content[:100]}...")
        
        try:
            response = await self._client.post(
                f"{self.host}/v1/jarvis",
                json=payload
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error: {e.response.status_code}")
            return {"status": "failed", "error": {"message": str(e)}}
        except httpx.RequestError as e:
            logger.error(f"Request failed: {e}")
            return {"status": "failed", "error": {"message": f"Connection failed: {e}"}}
    
    async def health_check(self) -> bool:
        try:
            response = await self._client.get(f"{self.host}/v1/health")
            return response.status_code == 200
        except:
            return False
    
    async def get_task(self, task_id: str) -> Optional[Dict[str, Any]]:
        try:
            response = await self._client.get(f"{self.host}/v1/task/{task_id}")
            if response.status_code == 200:
                return response.json()
        except:
            pass
        return None
    
    async def close(self):
        await self._client.aclose()
