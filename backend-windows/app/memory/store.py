import sqlite3
import aiosqlite
import os
import json
from typing import Optional, List, Dict, Any
from datetime import datetime
from app.config import settings
from app.logging.logger import logger

class MemoryStore:
    _db: Optional[aiosqlite.Connection] = None
    
    @classmethod
    async def initialize(cls):
        db_path = settings.memory_db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        cls._db = await aiosqlite.connect(db_path)
        cls._db.row_factory = aiosqlite.Row
        
        await cls._create_tables()
        logger.info(f"Memory store initialized: {db_path}")
    
    @classmethod
    async def _create_tables(cls):
        await cls._db.executescript("""
            CREATE TABLE IF NOT EXISTS episodic_memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                timestamp TEXT NOT NULL DEFAULT (datetime('now')),
                event_type TEXT NOT NULL,
                content TEXT NOT NULL,
                metadata TEXT
            );
            
            CREATE TABLE IF NOT EXISTS semantic_memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE NOT NULL,
                value TEXT NOT NULL,
                category TEXT DEFAULT 'general',
                confidence REAL DEFAULT 1.0,
                created_at TEXT NOT NULL DEFAULT (datetime('now')),
                updated_at TEXT NOT NULL DEFAULT (datetime('now'))
            );
            
            CREATE TABLE IF NOT EXISTS working_memory (
                session_id TEXT PRIMARY KEY,
                data TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now')),
                updated_at TEXT NOT NULL DEFAULT (datetime('now'))
            );
            
            CREATE INDEX IF NOT EXISTS idx_episodic_session ON episodic_memory(session_id);
            CREATE INDEX IF NOT EXISTS idx_episodic_timestamp ON episodic_memory(timestamp);
            CREATE INDEX IF NOT EXISTS idx_semantic_key ON semantic_memory(key);
            CREATE INDEX IF NOT EXISTS idx_semantic_category ON semantic_memory(category);
        """)
        await cls._db.commit()
    
    @classmethod
    async def execute(cls, query: str, params: tuple = ()) -> aiosqlite.Cursor:
        if cls._db is None:
            await cls.initialize()
        return await cls._db.execute(query, params)
    
    @classmethod
    async def executemany(cls, query: str, params: List[tuple]):
        if cls._db is None:
            await cls.initialize()
        return await cls._db.executemany(query, params)
    
    @classmethod
    async def commit(cls):
        if cls._db:
            await cls._db.commit()
    
    @classmethod
    async def close(cls):
        if cls._db:
            await cls._db.close()
            cls._db = None
            logger.info("Memory store closed")
