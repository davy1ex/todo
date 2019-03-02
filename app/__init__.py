from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


def create_app(): # инициализирует app
    app = Flask(__name__)
    app.config.from_object(Config)
    return app


app = create_app()
db = SQLAlchemy(app)
