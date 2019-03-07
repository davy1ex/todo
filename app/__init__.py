from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config


def create_app(): # инициализирует app
    app = Flask(__name__)
    app.config.from_object(Config)
    return app


app = create_app()
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = "login"
