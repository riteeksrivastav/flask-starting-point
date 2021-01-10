from flask import Blueprint, Response, request
import json
from http import HTTPStatus

user_module = Blueprint('user_module', __name__, url_prefix='/users')

@user_module.route('/', methods=['POST'])
def create_user():
    #get name, age from request body
    name = request.form.get('name')
    age = request.form.get('age')
        
    #Db call
    return Response(json.dumps({'message': 'User {} has been successfully registered'.format(name)}),
                status=HTTPStatus.OK,
                mimetype='application/json')