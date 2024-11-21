import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_random_number(client):
    response = client.get('/random')
    assert response.status_code == 200
    data = response.get_json()
    assert "number" in data
    assert 1 <= data["number"] <= 100

def test_even_odd(client):
    response = client.get('/even-odd/42')
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == "even"

    response = client.get('/even-odd/43')
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == "odd"