from app import db
from datetime import datetime


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
