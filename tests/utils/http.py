from types import TracebackType
from typing import Any, Self
from urllib.parse import urljoin

import requests


class SessionClient:
    """A simple HTTP client that uses requests.Session for connection pooling."""

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.session = requests.Session()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.session.close()
        if exc_type is not None or isinstance(exc_value, Exception):
            raise AssertionError(
                f"An error occurred during the session:\n{traceback}"
            ) from exc_value

    def _make_request(
        self, method: str, endpoint: str, **kwargs: Any
    ) -> requests.Response:
        """Make an HTTP request to the specified endpoint."""
        url = urljoin(self.base_url, endpoint)
        response = self.session.request(method.upper(), url, **kwargs)
        return response

    def get(self, endpoint: str, **kwargs: Any) -> requests.Response:
        """Send a GET request to the specified endpoint."""
        return self._make_request("GET", endpoint, **kwargs)

    def post(
        self, endpoint: str, data: Any = None, json: Any = None, **kwargs: Any
    ) -> requests.Response:
        """Send a POST request to the specified endpoint."""
        return self._make_request("POST", endpoint, data=data, json=json, **kwargs)

    def put(
        self, endpoint: str, data: Any = None, json: Any = None, **kwargs: Any
    ) -> requests.Response:
        """Send a PUT request to the specified endpoint."""
        return self._make_request("PUT", endpoint, data=data, json=json, **kwargs)

    def delete(self, endpoint: str, **kwargs: Any) -> requests.Response:
        """Send a DELETE request to the specified endpoint."""
        return self._make_request("DELETE", endpoint, **kwargs)
