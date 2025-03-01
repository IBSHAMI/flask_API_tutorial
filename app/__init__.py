from flask import Flask

from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register api blueprint
    from app.api.routes import api_blueprint

    app.register_blueprint(api_blueprint)

    return app
