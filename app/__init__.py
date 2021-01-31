import logging
import sys
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask.logging import default_handler


application = Flask(__name__)
application.config.from_object('config.AppConfig')

application.logger.removeHandler(default_handler)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(threadName)s - %(process)d - %(message)s'))
application.logger.addHandler(handler)
application.logger.setLevel(application.config["LOG_LEVEL"])

try:
    db = SQLAlchemy(application)
except Exception as e:
    application.logger.error('unable to initialize database, error{}'.format(e))

application.logger.info('database initialized successfully')

Migrate(application, db)
from app.user import db as user_db #this import is for the migration. All the modules should be included which need migration

from app.handler.ping import ping_module
from app.handler.user import user_module
application.register_blueprint(ping_module)
application.register_blueprint(user_module)