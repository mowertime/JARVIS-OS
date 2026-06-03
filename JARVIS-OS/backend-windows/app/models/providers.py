import httpx
import json
from typing import Optional, AsyncGenerator, Dict, Any
from app.models.base import BaseModel
from app.logging.logger import logger

class OllamaModel(BaseModel):
    def __init__(self, name: str, endpoint: str):
        self._name = name
        self._endpoint = endpoint
        self._client = httpx.AsyncClient(timeout=120.0)
        
        self._capabilities = {
            "code_generation": "deepseek" in name.lower(),
            "conversation": "llama" in name.lower(),
            "planning": "qwen" in name.lower(),
            "reasoning": "qwen" in name.lower() or "mistral" in name.lower(),
            "function_calling": True,
            "streaming": True
        }
    
    @property
    def model_name(self) -> str:
        return self._name
    
    @property
    def capabilities(self) -> Dict[str, bool]:
        return self._capabilities
    
    async def generate(self, prompt: str, system_prompt: Optional[str] = None,
                      temperature: float = 0.7, max_tokens: int = 2048) -> str:
        payload = {
            "model": self._name,
            "prompt": prompt,
            "system": system_prompt or "",
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": False
        }
        
        try:
            response = await self._client.post(self._endpoint, json=payload)
            response.raise_for_status()
            data = response.json()
            return data.get("response", "")
        except httpx.HTTPError as e:
            logger.error(f"Ollama {self._name} request failed: {e}")
            raise
        except Exception as e:
            logger.error(f"Model {self._name} error: {e}")
            raise
    
    async def generate_stream(self, prompt: str, system_prompt: Optional[str] = None,
                              temperature: float = 0.7, max_tokens: int = 2048) -> AsyncGenerator[str, None]:
        payload = {
            "model": self._name,
            "prompt": prompt,
            "system": system_prompt or "",
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": True
        }
        
        try:
            async with self._client.stream("POST", self._endpoint, json=payload) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if line.strip():
                        try:
                            data = json.loads(line)
                            chunk = data.get("response", "")
                            if chunk:
                                yield chunk
                        except json.JSONDecodeError:
                            continue
        except Exception as e:
            logger.error(f"Stream error for {self._name}: {e}")
            raise
    
    async def close(self):
        await self._client.aclose()


class MockModel(BaseModel):
    """Fallback model for development/testing without actual LLM"""
    def __init__(self, name: str = "mock"):
        self._name = name
    
    @property
    def model_name(self) -> str:
        return self._name
    
    @property
    def capabilities(self) -> Dict[str, bool]:
        return {"all": True}
    
    async def generate(self, prompt: str, system_prompt: Optional[str] = None,
                      temperature: float = 0.7, max_tokens: int = 2048) -> str:
        return f"[Mock {self._name}] Processing: {prompt[:100]}..."
    
    async def generate_stream(self, prompt: str, system_prompt: Optional[str] = None,
                              temperature: float = 0.7, max_tokens: int = 2048) -> AsyncGenerator[str, None]:
        yield f"[Mock {self._name}] Processing: {prompt[:100]}..."
