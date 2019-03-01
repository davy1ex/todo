import os


class Config():
    DEBUG = True
    SECRET_KEY = "RANDOM_KEY"
    # РАЗМЕТКА ДИРЕКТОРИИ ТОЛЬКО ПОД ЛИНУКС
    current_dir = os.getcwd()
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + current_dir + '/tasks.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
