from setuptools import setup, find_packages

setup(
    name="jarvis-frontend",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        "httpx",
        "pyaudio",
        "openai-whisper",
    ],
    entry_points={
        "console_scripts": [
            "jarvis-voice=voice.voice_service:main",
            "jarvis-agent=agent_client.client:main",
        ],
    },
)
