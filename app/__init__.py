"""Flask application package and factory."""

from flask import Flask

from app.config import Config
from app.errors import register_error_handlers
from app.logging_config import configure_logging
from app.routes import web_bp
from app.api.routes import api_bp


def create_app(config_class: type[Config] = Config) -> Flask:
	"""Application factory used by both development and production entrypoints."""
	app = Flask(
		__name__,
		static_folder="static",
		template_folder="templates",
	)
	app.config.from_object(config_class)

	configure_logging(app)
	register_error_handlers(app)

	app.register_blueprint(web_bp)
	app.register_blueprint(api_bp, url_prefix="/api")

	app.logger.info("Application initialized")
	return app
