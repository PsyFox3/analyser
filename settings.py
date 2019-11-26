import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

class settings():
    def __init__(self):
        # Init app
        app = Flask(__name__)
        basedir = os.path.abspath(os.path.dirname(__file__))

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.secret_key = 'mikey'
        api = Api(app)

        # Allowed extensions for the config file
        ALLOWED_EXTENSIONS = {'cfg'}
