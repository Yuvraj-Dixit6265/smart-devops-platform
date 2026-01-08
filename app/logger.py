import logging
from logging.handlers import RotatingFileHandler
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "..", "logs")
LOG_DIR = os.path.abspath(LOG_DIR)

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")

def setup_logger():
    logger = logging.getLogger("smart-devops")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = RotatingFileHandler(
            LOG_FILE,
            maxBytes=5_000_000,
            backupCount=3
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(levelname)s | %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

logger = setup_logger()
