"""REST API endpoints for client integrations."""

from flask import jsonify

from app.api.routes import api_bp


@api_bp.get("/health")
def health() -> tuple:
    """Lightweight health endpoint for uptime checks."""
    return jsonify({"status": "ok", "service": "rubiks-cube-solver-api"}), 200
