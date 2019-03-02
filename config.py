import os


class Config():
    DEBUG = True
    SECRET_KEY = "RANDOM_KEY"
    current_dir = os.getcwd() # текущая дирректория
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(current_dir, 'app', 'tasks.db') # склеивает воедино приставку sqlite, текущую дирректорию и папку для бд
    SQLALCHEMY_TRACK_MODIFICATIONS = False
