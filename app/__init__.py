from flask import Flask
from flask import Response
from http import HTTPStatus
import json

app = Flask(__name__)

@app.route('/ping')
def ping():
    return Response(json.dumps({'ping': 'pong'}),
                status=HTTPStatus.OK,
                mimetype='application/json')
    
if __name__ == '__main__':
    app.run()