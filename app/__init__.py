import os
from flask import Flask

from app.config.config import config_by_name

environment = os.getenv("FLASK_ENV") or "development"


def create_app():
    app = Flask(__name__)
    app.config.from_object(config_by_name[environment])

    from app.routes.auth import auth_blueprint

    app.register_blueprint(auth_blueprint)
    return app


configuration = config_by_name[environment]
