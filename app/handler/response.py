from http import HTTPStatus
from flask import Response
import json

def success(data):
    return Response(json.dumps({'message': data}),
                    status=HTTPStatus.OK,
                    mimetype='application/json')


def invalid_request(error):
    return Response(json.dumps({'error': error}),
                    status=HTTPStatus.BAD_REQUEST,
                    mimetype='application/json')


def internal_server_error(error):
    return Response(json.dumps({'error': error}),
                    status=HTTPStatus.INTERNAL_SERVER_ERROR,
                    mimetype='application/json')