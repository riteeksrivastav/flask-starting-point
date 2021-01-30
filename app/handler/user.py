from flask import Blueprint, Response, request
from http import HTTPStatus
import app.user.service as user_service
import app.user.exceptions as exceptions
import json
import logging

user_module = Blueprint('user_module', __name__, url_prefix='/users')

@user_module.route('/', methods=['POST'])
def create_user():
    logger = logging.getLogger('app.handler.user')
    
    #get name, age from request body
    name = request.form.get('name')
    age = request.form.get('age')
    if name == "" or age == "":
        logger.error('name or age should not be empty')
        return Response(json.dumps({'error': 'name or age should not be empty'.format(name)}),
                status=HTTPStatus.BAD_REQUEST,
                mimetype='application/json')

    try:
        user_service.create(name, age)
        logger.info('user with name {} has been successfully registers'.format(name))
        return Response(json.dumps({'message': 'User {} has been successfully registered'.format(name)}),
                status=HTTPStatus.OK,
                mimetype='application/json')
    except exceptions.UserAlreadyExists:
        logger.error('user with name {} already registerd'.format(name))
        return Response(json.dumps({'error': 'User {} is already registered'.format(name)}),
                status=HTTPStatus.BAD_REQUEST,
                mimetype='application/json')
    except Exception as e:
        logger.error('unable to register user with name {}, error: {}'.format(name, e))
        return Response(json.dumps({'error': 'something went wrong, please try after sometime'}),
                status=HTTPStatus.INTERNAL_SERVER_ERROR,
                mimetype='application/json')
    