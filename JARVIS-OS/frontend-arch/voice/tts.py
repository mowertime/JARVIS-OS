import asyncio
import subprocess
from typing import Optional, Callable
import logging

logger = logging.getLogger("jarvis.voice.tts")

class TTSEngine:
    def __init__(self, engine: str = "espeak"):
        self.engine = engine
        self.voice = "en-us"
    
    async def speak(self, text: str) -> bool:
        try:
            if self.engine == "espeak":
                subprocess.run(
                    ["espeak", "-v", self.voice, text],
                    capture_output=True, timeout=30
                )
                return True
            elif self.engine == "piper":
                subprocess.run(
                    ["piper", "--model", "/usr/share/piper/voices/en_US-lessac-medium.onnx",
                     "--output-raw", text],
                    capture_output=True, timeout=30
                )
                return True
            else:
                logger.warning(f"Unknown TTS engine: {self.engine}")
                return False
        except Exception as e:
            logger.error(f"TTS failed: {e}")
            return False
    
    async def speak_async(self, text: str, on_done: Optional[Callable] = None):
        result = await self.speak(text)
        if on_done:
            on_done(result)

class MockTTS(TTSEngine):
    def __init__(self):
        super().__init__("mock")
    
    async def speak(self, text: str) -> bool:
        logger.info(f"[TTS] {text}")
        await asyncio.sleep(0.2)
        return True
