# syntax=docker/dockerfile:1
FROM python:3.12-slim AS base

ENV POETRY_VERSION=2.0.1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_CACHE_DIR='/var/cache/pypoetry'
ENV POETRY_HOME='/usr/local'
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    git

COPY app /backend/app
COPY pyproject.toml /backend/pyproject.toml
WORKDIR /backend

RUN curl -sSL https://install.python-poetry.org | python - \
    && poetry --version \
    && poetry install --no-interaction --no-ansi

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
