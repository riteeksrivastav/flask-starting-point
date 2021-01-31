import pytest
from app import application

@pytest.fixture
def client():
    test_app = application
    test_app.config['TESTING'] = True
    yield test_app.test_client()

def test_ping(client):
    response = client.get("/ping", content_type="application/json")
    assert response.status_code == 200
    assert response.json == {'ping': 'pong'}
