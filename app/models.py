from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password_hash = db.Column(db.String(128))
    tasks = db.relationship("Task", backref="master", lazy="dynamic")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<user: {}>".format(self.username)


class Task(db.Model):
    """ модель, задающая задачу """
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    created = db.Column(db.Integer, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    self_id = db.Column(db.Integer)

    # def __init__(self, *args, **kwargs):
    #     super(Task, self).__init__(*args, **kwargs)

    def __repr__(self):
        """ возвращает красивую информацию о задаче """
        return '<id: {0} body: {1}>'.format(self.id, self.body)
