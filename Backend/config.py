import os

basedir = os.path.abspath(os.path.dirname(__file__))
current_directory_path = os.getcwd()


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "prodoscore@2020"

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:admin@localhost:5432/assessment'
    SQLALCHEMY_TRACK_MODIFICATIONS = False