import pytest
import json
import os
import mock

os.environ['ENV'] = 'TEST' #This is to get the db connection from test_db
from app import application, db
del os.environ['ENV'] #Del the environment variable to make app state same as before 

from app.user.db import Users
from sqlalchemy import delete

@pytest.fixture
def client():
    test_app = application
    test_app.config['TESTING'] = True
    yield test_app.test_client()
    
def clean_db():
    table = Users.__table__
    stmt = delete(table)
    db.session.execute(stmt)
    db.session.commit()
    db.session.close()

# The db has not been mocked to test the end to end behavior, we can mock the db.
def test_should_return_success_for_valid_request(client):
    clean_db()
    response = client.post("/users",  data={'name': "Bob", 'age': "23"})
    
    assert response.status_code == 200
    assert response.json == {'message': 'User Bob has been successfully registered'}
    clean_db()
    
def test_should_return_bad_request_for_either_name_or_age_empty(client):
    response = client.post("/users")
    
    assert response.status_code == 400
    assert response.json == {'error': 'name or age should not be empty'}
    
def test_should_return_user_already_registerd_when_user_is_already_exists(client):
    clean_db()
    client.post("/users",  data={'name': "Bob", 'age': "23"})
    
    response = client.post("/users",  data={'name': "Bob", 'age': "23"})
    assert response.status_code == 400
    assert response.json == {'error': 'User Bob is already registered'}
    clean_db()
    
def test_should_return_internal_server_error_when_some_uncaught_exception_occured(client, mocker):
    mocker.patch('app.user.service.create', side_effect=Exception('table not found'))
    response = client.post("/users",  data={'name': "Bob", 'age': "23"})
    
    assert response.status_code == 500
    assert response.json == {'error': 'something went wrong, please try after sometime'}
     