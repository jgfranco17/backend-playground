import pytest
from fastapi.testclient import TestClient

from api.service import app


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--with-integration",
        action="store_true",
        default=False,
        help="Run integration tests.",
    )


def requires_integration(test_case_id: str) -> pytest.MarkDecorator:
    """Skip a test unless --with-integration was passed on the CLI."""
    return pytest.mark.skipif(
        "not config.getoption('--with-integration')",
        reason=f"[{test_case_id}] Requires --with-integration flag.",
    )


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
