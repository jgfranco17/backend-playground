from collections.abc import Iterator

import pytest

from tests.conftest import requires_integration
from tests.utils.http import SessionClient


class TestIntegration:
    """Integration tests for the API endpoints."""

    BASE_URL = "http://localhost:8000"

    @pytest.fixture(scope="class")
    def session(self) -> Iterator[SessionClient]:
        headers: dict[str, str] = {
            "Content-Type": "application/json",
            "is-test": "true",
        }
        with SessionClient(self.BASE_URL) as session:
            session.session.headers.update(headers)
            yield session

    @pytest.mark.integration
    @requires_integration("INTEGRATION-001")
    def test_index_url(self, session: SessionClient) -> None:
        response = session.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, world!"}

    @pytest.mark.integration
    @requires_integration("INTEGRATION-002")
    def test_health_endpoint(self, session: SessionClient) -> None:
        response = session.get("/healthz")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}, (
            "Health endpoint should return healthy status."
        )

    @pytest.mark.integration
    @requires_integration("INTEGRATION-003")
    def test_nonexistent_routes(self, session: SessionClient) -> None:
        response = session.get("/non-existent")
        assert response.status_code == 404, "Endpoint should not exist in API."

    @pytest.mark.integration
    @requires_integration("INTEGRATION-004")
    def test_greet_endpoint_success(self, session: SessionClient) -> None:
        name = "John"
        response = session.get(f"/v0/greet?name={name}")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, John!"}

    @pytest.mark.integration
    @requires_integration("INTEGRATION-005")
    def test_greet_endpoint_fail_no_name(self, session: SessionClient) -> None:
        response = session.get("/v0/greet")
        assert response.status_code == 400
        assert "Name cannot be empty" in response.json()["message"]
