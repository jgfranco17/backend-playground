import logging
from http import HTTPStatus
from typing import Any, Callable, Dict

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.routes.v0.routes import router_v0

logger = logging.getLogger(__name__)


app = FastAPI(
    title="Backend Playground API",
    summary="Basic sample API",
    description="Simple REST API for developer experiments",
)


@app.get("/")
def read_index() -> Dict[str, str]:
    return {"message": "Hello, world!"}


@app.get("/healthz")
def check_api_health() -> Dict[str, str]:
    return {"status": "healthy"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """General exception handler."""
    logger.error(
        f"Service encountered HTTP {exc.status_code} error from {request.method}: {exc.detail}"
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": exc.status_code, "message": exc.detail},
    )


# Load routes and middlewares
app.include_router(router_v0)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to restrict origins
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
