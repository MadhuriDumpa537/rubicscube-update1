"""Web-facing routes for HTML pages."""

from flask import render_template

from app.routes import web_bp


@web_bp.get("/")
def home() -> str:
    """Render the homepage."""
    return render_template("index.html")


@web_bp.get("/upload")
def upload_page() -> str:
    """Render upload page shell. Processing is intentionally not implemented yet."""
    return render_template("upload.html")
