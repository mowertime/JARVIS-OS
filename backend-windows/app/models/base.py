from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, AsyncGenerator

class BaseModel(ABC):
    @abstractmethod
    async def generate(self, prompt: str, system_prompt: Optional[str] = None, 
                      temperature: float = 0.7, max_tokens: int = 2048) -> str:
        pass
    
    @abstractmethod
    async def generate_stream(self, prompt: str, system_prompt: Optional[str] = None,
                             temperature: float = 0.7, max_tokens: int = 2048) -> AsyncGenerator[str, None]:
        pass
    
    @property
    @abstractmethod
    def model_name(self) -> str:
        pass
    
    @property
    @abstractmethod
    def capabilities(self) -> Dict[str, bool]:
        pass
