"""Centralized HTTP error handlers."""

from flask import Flask, jsonify, render_template, request


def _wants_json() -> bool:
    """Detect if the request expects a JSON response."""
    return request.path.startswith("/api") or request.accept_mimetypes.best == "application/json"


def register_error_handlers(app: Flask) -> None:
    """Register consistent error responses for web and API routes."""

    @app.errorhandler(404)
    def not_found(error):  # type: ignore[unused-argument]
        if _wants_json():
            return jsonify({"error": "Not Found", "message": "Resource does not exist."}), 404
        return render_template("errors/404.html"), 404

    @app.errorhandler(405)
    def method_not_allowed(error):  # type: ignore[unused-argument]
        if _wants_json():
            return jsonify({"error": "Method Not Allowed", "message": "HTTP method is not allowed."}), 405
        return render_template("errors/405.html"), 405

    @app.errorhandler(500)
    def server_error(error):  # type: ignore[unused-argument]
        app.logger.exception("Unhandled server error: %s", error)
        if _wants_json():
            return jsonify({"error": "Internal Server Error", "message": "Unexpected error occurred."}), 500
        return render_template("errors/500.html"), 500
