# syntax=docker/dockerfile:1
FROM python:3.13-alpine AS base

ENV UV_PROJECT_ENVIRONMENT=/usr/local
ENV UV_LINK_MODE=copy
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

FROM base AS builder

RUN apk add --no-cache build-base curl git

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY api/ /backend/api
COPY pyproject.toml uv.lock /backend/
WORKDIR /backend

RUN uv --version \
    && uv sync --no-dev --locked

FROM builder AS app

WORKDIR /backend
EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
