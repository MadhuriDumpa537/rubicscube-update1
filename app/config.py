"""Application configuration module."""

import os


class Config:
    """Base app configuration."""

    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    ENV = os.getenv("FLASK_ENV", "development")
    DEBUG = ENV == "development"
    TESTING = False
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_DIR = os.getenv("LOG_DIR", "logs")


class DevelopmentConfig(Config):
    """Development settings."""


class TestingConfig(Config):
    """Testing settings."""

    TESTING = True


class ProductionConfig(Config):
    """Production settings."""

    DEBUG = False
