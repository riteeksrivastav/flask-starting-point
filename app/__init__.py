from flask import Flask
from http import HTTPStatus
import json

application = Flask(__name__)
    
from app.handler.ping import ping_module
from app.handler.user import user_module
application.register_blueprint(ping_module)
application.register_blueprint(user_module)