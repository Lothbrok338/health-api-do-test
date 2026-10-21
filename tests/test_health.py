"""Check the explicit API contract and that unknown routes remain unavailable."""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health_contract():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}


def test_unrecognized_route():
    response = client.get('/not-found')
    assert response.status_code == 404
