"""Web route blueprint package."""

from flask import Blueprint

web_bp = Blueprint("web", __name__)

from app.routes import routes  # noqa: E402,F401
