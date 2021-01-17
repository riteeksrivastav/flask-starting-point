from flask import Blueprint, Response, request
import json
from http import HTTPStatus
import app.user.service as user_service
import app.user.exceptions as exceptions

user_module = Blueprint('user_module', __name__, url_prefix='/users')

@user_module.route('/', methods=['POST'])
def create_user():
    #get name, age from request body
    name = request.form.get('name')
    age = request.form.get('age')

    try:
        user_service.create(name, age)
        return Response(json.dumps({'message': 'User {} has been successfully registered'.format(name)}),
                status=HTTPStatus.OK,
                mimetype='application/json')
    except exceptions.UserAlreadyExists:
        return Response(json.dumps({'error': 'User {} is already registered'.format(name)}),
                status=HTTPStatus.BAD_REQUEST,
                mimetype='application/json')
    