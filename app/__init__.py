import os
from flask import Flask

from app.config.config import config_by_name

environment = os.getenv("FLASK_ENV") or "development"


def create_app():
    app = Flask(__name__)
    app.config.from_object(config_by_name[environment])

    from app.routes.auth import github_blueprint

    app.register_blueprint(github_blueprint, url_prefix="/login")

    return app


configuration = config_by_name[environment]
