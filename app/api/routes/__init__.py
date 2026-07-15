"""API routes blueprint package."""

from flask import Blueprint

api_bp = Blueprint("api", __name__)

from app.api.routes import routes  # noqa: E402,F401
