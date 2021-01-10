from flask import Blueprint, Response
import json
from http import HTTPStatus

ping_module = Blueprint('ping', __name__, url_prefix='')

@ping_module.route('/ping')
def ping():
    return Response(json.dumps({'ping': 'pong'}),
                status=HTTPStatus.OK,
                mimetype='application/json')