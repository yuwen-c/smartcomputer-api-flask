import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DATABASE_NAME = 'sqlite.db'
    DATABASE_PATH = os.path.join(basedir, 'database', DATABASE_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False

