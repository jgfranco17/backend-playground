from typing import List

import pytest
from fastapi.testclient import TestClient


def test_index_url(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}


def test_health_endpoint(client: TestClient):
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


@pytest.mark.parametrize("endpoint", ["random", "doesnt-exist", "fail"])
def test_nonexistent_routes(client: TestClient, endpoint: str):
    response = client.get(f"/{endpoint}")
    assert response.status_code == 404, "Endpoint should not exist in API."


def test_greet_endpoint_success(client: TestClient):
    response = client.get("/v0/greet?name=John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John!"}


def test_greet_endpoint_fail_no_name(client: TestClient):
    response = client.get("/v0/greet")
    assert response.status_code == 400
    assert "Name cannot be empty" in response.json()["message"]
