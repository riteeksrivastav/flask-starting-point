from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config.from_object('config.AppConfig')

db = SQLAlchemy(application)
Migrate(application, db)
from app.user import db as user_db

from app.handler.ping import ping_module
from app.handler.user import user_module
application.register_blueprint(ping_module)
application.register_blueprint(user_module)