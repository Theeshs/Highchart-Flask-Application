from flask import Flask

from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail
# from flask_sse import sse
from application.hub import execute_adding_data
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
import threading
from concurrent import futures
from werkzeug.exceptions import HTTPException
from flask import jsonify
from application.models import db

app = Flask(__name__, static_url_path='/static/')
app.config.from_object(Config)
CORS(app)

# jwt = JWTManager(app)
migrate = Migrate(app, db)
mail = Mail(app)


# mysql = MySQL(app)

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


executors = {
    'default': ThreadPoolExecutor(16),
    'processpool': ProcessPoolExecutor(4)
}

file_purger_executors = {
    'default': ThreadPoolExecutor(1),
    'processpool': ProcessPoolExecutor(1)
}

file_checksum_executors = {
    'default': ThreadPoolExecutor(1),
    'processpool': ProcessPoolExecutor(1)
}

pool = futures.ThreadPoolExecutor(max_workers=50)

from application import api

db.init_app(app)

# app.register_blueprint(sse, url_prefix='/stream')
db.app = app
db.create_all()


def create():
    hub.execute_adding_data()
    # print('started')
    # for i in range(0, 10000000):
    #     pool.submit(execute_adding_data())
    # pool.shutdown()


create()
