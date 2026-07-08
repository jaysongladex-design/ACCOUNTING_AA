"""
Reusable helper functions for the AirAsia project.

Right now this sets up logging so your program can print nice, timestamped
messages both to the screen and to a file in the "logs/" folder.
"""

import logging
import os
from datetime import datetime


def get_logger(name: str = "airasia") -> logging.Logger:
    """Create and return a logger that writes to the screen and to a log file.

    Example:
        log = get_logger()
        log.info("Starting up!")
    """
    # Figure out the project's root folder and make sure "logs/" exists.
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    logs_dir = os.path.join(project_root, "logs")
    os.makedirs(logs_dir, exist_ok=True)

    log_level = os.getenv("LOG_LEVEL", "INFO").upper()

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Avoid adding duplicate handlers if this function is called more than once.
    if logger.handlers:
        return logger

    log_format = logging.Formatter(
        "%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # 1) Show messages on the screen.
    console = logging.StreamHandler()
    console.setFormatter(log_format)
    logger.addHandler(console)

    # 2) Also save messages to a dated log file.
    today = datetime.now().strftime("%Y-%m-%d")
    file_handler = logging.FileHandler(
        os.path.join(logs_dir, f"{today}.log"), encoding="utf-8"
    )
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    return logger
