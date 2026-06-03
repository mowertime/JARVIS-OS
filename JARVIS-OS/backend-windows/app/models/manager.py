from typing import Dict, Any, Optional, AsyncGenerator
from app.models.providers import OllamaModel, MockModel
from app.models.base import BaseModel
from app.config import settings
from app.logging.logger import logger

class ModelManager:
    def __init__(self):
        self._models: Dict[str, BaseModel] = {}
        self._initialize_models()
    
    def _initialize_models(self):
        try:
            self._models["qwen2.5"] = OllamaModel("qwen2.5", settings.qwen_endpoint)
            self._models["llama3"] = OllamaModel("llama3", settings.llama_endpoint)
            self._models["deepseek-coder"] = OllamaModel("deepseek-coder", settings.deepseek_endpoint)
            self._models["mistral"] = OllamaModel("mistral", settings.mistral_endpoint)
            logger.info("All Ollama models initialized")
        except Exception as e:
            logger.warning(f"Failed to initialize Ollama models: {e}. Using mock models.")
            self._models["qwen2.5"] = MockModel("qwen2.5")
            self._models["llama3"] = MockModel("llama3")
            self._models["deepseek-coder"] = MockModel("deepseek-coder")
            self._models["mistral"] = MockModel("mistral")
    
    def get_model(self, name: str) -> BaseModel:
        model = self._models.get(name)
        if not model:
            logger.warning(f"Model {name} not found, falling back to qwen2.5")
            model = self._models.get("qwen2.5", MockModel("fallback"))
        return model
    
    async def generate_response(self, model_name: str, prompt: str, 
                               system_prompt: Optional[str] = None, **kwargs) -> str:
        model = self.get_model(model_name)
        logger.debug(f"Generating response with {model_name}")
        return await model.generate(prompt, system_prompt, **kwargs)
    
    async def query_model(self, model_name: str, prompt: str, **kwargs) -> str:
        return await self.generate_response(model_name, prompt, **kwargs)
    
    async def generate_stream(self, model_name: str, prompt: str,
                             system_prompt: Optional[str] = None) -> AsyncGenerator[str, None]:
        model = self.get_model(model_name)
        async for chunk in model.generate_stream(prompt, system_prompt):
            yield chunk
    
    def list_models(self) -> Dict[str, Any]:
        return {
            name: {
                "capabilities": model.capabilities,
                "type": type(model).__name__
            }
            for name, model in self._models.items()
        }
    
    async def close_all(self):
        for name, model in self._models.items():
            if hasattr(model, "close"):
                try:
                    await model.close()
                except Exception as e:
                    logger.warning(f"Error closing model {name}: {e}")
