from flask import Flask
#from flask_cors import CORS

from app.main.config import config_by_name
from app.main.logconfig import LogSetup

def create_app(config_name):
    app = Flask(__name__, template_folder='static/templates/')
    app.config.from_object(config_by_name[config_name])
    register_extensions(app)

    return app

def register_extensions(app):
    logs = LogSetup()
    logs.init_app(app)