import asyncio
from typing import Optional, Callable
import logging

logger = logging.getLogger("jarvis.voice.stt")

class STTEngine:
    def __init__(self, engine: str = "whisper"):
        self.engine = engine
        self._model = None
    
    async def initialize(self):
        if self.engine == "whisper":
            try:
                import whisper
                self._model = whisper.load_model("base")
                logger.info("Whisper STT model loaded")
            except ImportError:
                logger.warning("Whisper not available, using mock")
                self._model = "mock"
        else:
            logger.info(f"STT engine set to: {self.engine}")
    
    async def transcribe(self, audio_path: str) -> str:
        if self._model == "mock":
            await asyncio.sleep(0.5)
            return "Simulated speech to text output"
        
        if self.engine == "whisper" and self._model:
            import whisper
            result = self._model.transcribe(audio_path)
            return result.get("text", "")
        
        return ""
    
    async def transcribe_stream(self, audio_stream) -> str:
        if self._model == "mock":
            await asyncio.sleep(0.3)
            return "Simulated streaming transcription"
        return ""

class MockSTT(STTEngine):
    def __init__(self):
        super().__init__("mock")
    
    async def transcribe(self, audio_path: str) -> str:
        await asyncio.sleep(0.3)
        return "mock transcription"
