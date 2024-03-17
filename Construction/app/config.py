import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://your_username:your_password@localhost/your_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
