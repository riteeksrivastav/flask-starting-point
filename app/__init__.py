from flask import Flask
from flask import Response
from http import HTTPStatus
import json

application = Flask(__name__)

@application.route('/ping')
def ping():
    return Response(json.dumps({'ping': 'pong'}),
                status=HTTPStatus.OK,
                mimetype='application/json')
