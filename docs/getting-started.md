# Getting Started

This page walks through setting up Backend Playground locally, running it either
directly or via Docker, and running the test suite.

## Prerequisites

Make sure the following are installed:

- [Python 3.13](https://www.python.org/downloads/release/python-3130/) or above
- [Docker](https://docs.docker.com/engine/install/)
- [UV](https://docs.astral.sh/uv/getting-started/) for dependency management
- [just](https://github.com/casey/just) (optional, but the `justfile` wraps every
  command shown below)

## Clone and install

```bash
git clone https://github.com/jgfranco17/backend-playground.git
cd backend-playground
uv sync
```

`uv sync` creates a virtual environment and installs both the runtime and development
dependency groups defined in `pyproject.toml`.

## Running the API

With uv directly:

```bash
uv run uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

Or with `just`:

```bash
just start
```

Once running, the API is available at `http://localhost:8000`. Visit
`http://localhost:8000/docs` for the interactive Swagger UI that FastAPI generates
automatically.

## Running via Docker Compose

The API also ships with a `Dockerfile` and `compose.yaml` so it can run in a container
without a local Python environment:

```bash
# Build the image
just build

# Start the full stack
just up

# Stop it
just down
```

This builds the image from the Alpine-based `Dockerfile` and exposes the API on
`localhost:8000`, with a Docker healthcheck polling `/healthz`.

!!! note
    `compose.yaml` includes a commented-out Postgres service intended to back the
    schema in `migrations/`. It isn't wired up yet - see [Architecture](architecture.md#database)
    for details.

## Running tests

Unit tests use FastAPI's `TestClient` and don't require a running server:

```bash
just pytest
```

Integration tests exercise a live instance of the API over HTTP and are skipped by
default. Start the API first (locally or via Docker), then run:

```bash
just pytest --with-integration
```

Both `just pytest` variants accept extra pytest arguments after the flags, e.g.
`just pytest -k greet -v`.

## Building the docs locally

This documentation site is built with [MkDocs](https://www.mkdocs.org/) and the
Material theme. To preview it locally:

```bash
just docs
```

This runs `mkdocs build --strict --clean` followed by `mkdocs serve --open`, which
opens a live-reloading preview in your browser.
