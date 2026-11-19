
from app import app


def test_homepage():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"version 1" in response.data


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_info():
    client = app.test_client()
    response = client.get("/api/info")

    assert response.status_code == 200
    assert response.get_json()["version"] == "1"


def test_invalid_page():
    client = app.test_client()
    response = client.get("/does-not-exist")

    assert response.status_code == 404
