import logging
import os
import time
from http import HTTPStatus
from typing import Any, Callable, Dict

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.routes.v0.routes import router_v0

app = FastAPI(
    title="Backend Playground API",
    summary="Basic sample API",
    description="Simple REST API for developer experiments",
)


@app.get("/")
def read_index():
    return {"message": "Hello, world!"}


@app.get("/healthz")
def read_root():
    return {"status": "healthy"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """General exception handler."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": exc.status_code, "message": exc.detail},
    )


app.include_router(router_v0)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to restrict origins
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
