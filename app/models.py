from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class Task(db.Model):
    """ модель, задающая задачу """
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    created = db.Column(db.Integer, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)

    def __repr__(self):
        """ возвращает красивую информацию о задаче """
        return '<id: {0} body: {1}>'.format(self.id, self.body)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.passworh_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<user: {}>".fromat(self.username)
