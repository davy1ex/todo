from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app

# def del_task(self, id):
#     db.session.delete(Task.query.filter_by(id=id).first())
#     db.session.commit()


app = create_app()
db = SQLAlchemy(app)

# app.jinja_env.globals.update(clever_function=del_task)
