from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    import app.mainlist.controllers as mainlist

    app.register_blueprint(mainlist.module)

    return app
