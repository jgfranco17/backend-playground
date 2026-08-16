import time
from collections.abc import Awaitable, Callable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from api.observability.metrics import REQUEST_COUNT, REQUEST_LATENCY

type DispatchCallable = Callable[[Request], Awaitable[Response]]


class PrometheusMiddleware(BaseHTTPMiddleware):
    """Middleware to collect Prometheus metrics for HTTP requests."""

    async def dispatch(self, request: Request, call_next: DispatchCallable) -> Response:
        start_time = time.perf_counter()
        response = await call_next(request)
        duration = time.perf_counter() - start_time

        path = _resolve_route_path(request)
        REQUEST_LATENCY.labels(method=request.method, path=path).observe(duration)
        REQUEST_COUNT.labels(
            method=request.method,
            path=path,
            status_code=response.status_code,
        ).inc()

        return response


def _resolve_route_path(request: Request) -> str:
    """Use the matched route template to keep label cardinality low."""
    route = request.scope.get("route")
    return route.path if route else request.url.path
