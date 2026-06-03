import asyncio
import json
import httpx
from typing import Optional
from voice.wake_word import WakeWordDetector, WAKE_RESPONSE
from voice.stt import STTEngine
from voice.tts import TTSEngine
import logging

logger = logging.getLogger("jarvis.voice.service")

class VoiceService:
    def __init__(self, windows_host: str = "http://localhost:8000"):
        self.windows_host = windows_host
        self.wake_detector = WakeWordDetector()
        self.stt = STTEngine()
        self.tts = TTSEngine()
        self.http_client = httpx.AsyncClient(timeout=30.0)
        self.is_running = False
        
        self.wake_detector.on_wake = self._on_wake_detected
    
    async def initialize(self):
        await self.stt.initialize()
        logger.info("Voice service initialized")
    
    async def _on_wake_detected(self):
        logger.info("Wake word detected")
        await self.tts.speak(WAKE_RESPONSE)
        await self._listen_and_process()
    
    async def _listen_and_process(self):
        audio_file = "/tmp/jarvis_voice_input.wav"
        
        text = await self.stt.transcribe(audio_file)
        if not text:
            logger.warning("No speech detected")
            return
        
        logger.info(f"STT result: {text}")
        
        try:
            response = await self.http_client.post(
                f"{self.windows_host}/v1/jarvis",
                json={
                    "session_id": "arch-voice-session",
                    "timestamp": asyncio.get_event_loop().time(),
                    "input_type": "voice",
                    "content": text,
                    "context": {"device": "arch", "state": "active"}
                }
            )
            
            result = response.json()
            output = result.get("output", "I couldn't process that request.")
            
            await self.tts.speak(output)
            
        except Exception as e:
            logger.error(f"Request to Windows node failed: {e}")
            await self.tts.speak("I encountered a network error. Please check the connection.")
    
    async def start(self):
        self.is_running = True
        logger.info("Voice service started")
        
        while self.is_running:
            await self.wake_detector.detect_loop()
            await asyncio.sleep(0.1)
    
    async def stop(self):
        self.is_running = False
        self.wake_detector.stop()
        await self.http_client.aclose()
        logger.info("Voice service stopped")
