import pytest
import app.user.service as user_service
from app.user.exceptions import UserAlreadyExists

def test_should_successfully_create_user(mocker):
    def sample_create(arg1, arg2):
        return None
    mocker.patch('app.user.service.Users.create', sample_create)
    assert user_service.create('Bob', 23) == None
    
def test_should_raise_already_exist_exception_when_user_presents(mocker):
    mocker.patch('app.user.service.Users.create', side_effect=UserAlreadyExists)
    with pytest.raises(UserAlreadyExists):
        user_service.create('Bob', 23)
        
def test_should_propogate_exception_when_uncaught_exception_occures(mocker):
    mocker.patch('app.user.service.Users.create', side_effect=Exception('something went wrong'))
    with pytest.raises(Exception):
        user_service.create('Bob', 23)