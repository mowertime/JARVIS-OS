import logging
import sys
import os
from app.config import settings

def setup_logging():
    os.makedirs(os.path.dirname(settings.log_file), exist_ok=True)
    
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    file_handler = logging.FileHandler(settings.log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(getattr(logging, settings.log_level.upper()))
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(getattr(logging, settings.log_level.upper()))
    
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, settings.log_level.upper()))
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    return root_logger

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)

logger = get_logger("jarvis")
