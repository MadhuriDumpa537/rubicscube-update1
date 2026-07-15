"""Application logging configuration."""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from flask import Flask


def configure_logging(app: Flask) -> None:
    """Configure console and rotating file logging."""
    log_dir = Path(app.config.get("LOG_DIR", "logs"))
    log_dir.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        log_dir / "app.log",
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    app.logger.handlers.clear()
    app.logger.addHandler(stream_handler)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(app.config.get("LOG_LEVEL", "INFO"))
