from flask import Blueprint, Response, request
from http import HTTPStatus
import app.handler.response as resp
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
        return resp.invalid_request('name or age should not be empty'.format(name))

    try:
        user_service.create(name, age)
        logger.info('user with name {} has been successfully registered'.format(name))
        return resp.success('User {} has been successfully registered'.format(name))
    except exceptions.UserAlreadyExists:
        logger.error('user with name {} already registerd'.format(name))
        return resp.invalid_request('User {} is already registered'.format(name))
    except Exception as e:
        logger.error('unable to register user with name {}, error: {}'.format(name, e))
        return resp.internal_server_error('something went wrong, please try after sometime')
    