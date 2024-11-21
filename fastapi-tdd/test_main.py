from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_create_item():
    response = client.post("/items/", json={"name": "Test Item", "price": 10.5})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Test Item", "price": 10.5}