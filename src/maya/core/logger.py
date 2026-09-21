import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler
from maya.core.config import config

def setup_logger(name: str = "maya") -> logging.Logger:
    """Configures and returns a logger instance for MAYA."""
    logger = logging.getLogger(name)
    
    # Avoid duplicate handlers if setup_logger is called multiple times
    if logger.handlers:
        return logger
        
    logger.setLevel(logging.DEBUG if config.debug else logging.INFO)
    
    # Create logs directory
    root_dir = Path(__file__).resolve().parent.parent.parent.parent
    log_dir = root_dir / "logs"
    log_dir.mkdir(exist_ok=True)
    
    log_file = log_dir / "maya.log"
    
    # File handler (Rotating, max 5MB, keep 3 backups)
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=3, encoding="utf-8"
    )
    file_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_format)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_format = logging.Formatter(
        "%(levelname)s: %(message)s"
    )
    console_handler.setFormatter(console_format)
    
    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

logger = setup_logger()
