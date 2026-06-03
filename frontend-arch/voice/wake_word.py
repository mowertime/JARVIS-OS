import asyncio
import pyaudio
import struct
import math
from typing import Optional, Callable
from dataclasses import dataclass
import logging

logger = logging.getLogger("jarvis.voice.wake")

WAKE_WORD = "hey jarvis"
WAKE_RESPONSE = "Go ahead, sir."

@dataclass
class AudioConfig:
    rate: int = 16000
    chunk: int = 1024
    channels: int = 1
    format: int = pyaudio.paInt16
    threshold: float = 0.02
    silence_seconds: float = 1.5

class WakeWordDetector:
    def __init__(self, config: Optional[AudioConfig] = None):
        self.config = config or AudioConfig()
        self.audio = pyaudio.PyAudio()
        self.stream: Optional[pyaudio.Stream] = None
        self.is_running = False
        self.on_wake: Optional[Callable] = None
    
    def _rms(self, data: bytes) -> float:
        count = len(data) // 2
        if count == 0:
            return 0.0
        fmt = f"{count}h"
        try:
            samples = struct.unpack(fmt, data)
            sum_squares = sum(s * s for s in samples)
            return math.sqrt(sum_squares / count) / 32768.0
        except struct.error:
            return 0.0
    
    def start(self):
        self.stream = self.audio.open(
            format=self.config.format,
            channels=self.config.channels,
            rate=self.config.rate,
            input=True,
            frames_per_buffer=self.config.chunk
        )
        self.is_running = True
        logger.info("Wake word detection started")
    
    def stop(self):
        self.is_running = False
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.audio.terminate()
        logger.info("Wake word detection stopped")
    
    async def detect_loop(self):
        if not self.stream:
            self.start()
        
        while self.is_running:
            try:
                data = self.stream.read(self.config.chunk, exception_on_overflow=False)
                level = self._rms(data)
                
                if level > self.config.threshold:
                    logger.debug(f"Audio level: {level:.4f}")
                    if self.on_wake:
                        self.on_wake()
                        await asyncio.sleep(2)
                
                await asyncio.sleep(0.01)
            except Exception as e:
                logger.error(f"Wake detection error: {e}")
                await asyncio.sleep(0.1)


class SimpleWakeDetector:
    """Simplified wake word detection using energy-based voice activity"""
    def __init__(self, threshold: float = 500):
        self.threshold = threshold
        self.is_running = False
        self.on_wake: Optional[Callable] = None
        self._silence_chunks = 0
        self._max_silence_chunks = 30
    
    async def process_audio_level(self, level: float):
        if level > self.threshold:
            self._silence_chunks = 0
            if self.on_wake:
                self.on_wake()
        else:
            self._silence_chunks += 1
