import pytest

from src.app import __version__, app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_index(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Usine logicielle", "version": __version__}


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_version(client):
    response = client.get("/version")

    assert response.status_code == 200
    assert response.get_json() == {"version": __version__}


def test_not_found(client):
    response = client.get("/missing")

    assert response.status_code == 404
