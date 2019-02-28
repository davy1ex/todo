import os


class Config():
    DEBUG = True
    # defendes
    # CSRF_ENABLED = True
    # random key for acces
    SECRET_KEY = "RANDOM_KEY"
    # URI for database
    SQLALCHEMY_DATABASE_URI = 'sqlite:////home/davy1ex/mycode/python/todo/app/tasks.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
