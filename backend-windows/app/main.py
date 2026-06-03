import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.routes import router
from app.logging.logger import setup_logging
import asyncio

app = FastAPI(title=settings.app_name, version=settings.version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/v1")

@app.on_event("startup")
async def startup():
    setup_logging()
    from app.logging.logger import logger
    logger.info(f"{settings.app_name} v{settings.version} starting")
    from app.memory.store import MemoryStore
    await MemoryStore.initialize()

@app.on_event("shutdown")
async def shutdown():
    from app.logging.logger import logger
    logger.info("JARVIS OS shutting down")
    from app.memory.store import MemoryStore
    await MemoryStore.close()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=settings.host, port=settings.port, reload=settings.debug)
