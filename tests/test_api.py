from fastapi.testclient import TestClient


def test_index_url(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}


def test_health_endpoint(client: TestClient) -> None:
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_nonexistent_routes(client: TestClient) -> None:
    response = client.get("/non-existent")
    assert response.status_code == 404, "Endpoint should not exist in API."


def test_greet_endpoint_success(client: TestClient) -> None:
    response = client.get("/v0/greet?name=John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John!"}


def test_greet_endpoint_fail_no_name(client: TestClient) -> None:
    response = client.get("/v0/greet")
    assert response.status_code == 400
    assert "Name cannot be empty" in response.json()["message"]
