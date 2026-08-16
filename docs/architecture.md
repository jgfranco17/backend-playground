# Architecture

A tour of how the project is laid out and how the pieces connect.

## Application

The FastAPI app is assembled in `api/service.py`:

- A single `FastAPI` instance is created with title/description metadata.
- Root-level routes (`/`, `/healthz`) are declared directly on `app`.
- Versioned routes are defined on an `APIRouter` in `api/routes/v0/routes.py` with the
  `/v0` prefix, then mounted via `app.include_router(router_v0)`.
- A shared handler intercepts every `HTTPException` and logs it, returning a
  consistent `{status, message}` JSON body instead of FastAPI's default error shape.
- CORS middleware is attached last, currently allowing all origins for `GET` requests.

`api/main.py` is the process entry point: it imports the `app` object and runs it with
`uvicorn.run(...)`. In practice, both `just start` and the Dockerfile invoke `uvicorn`
directly against `api.main:app` rather than calling `run()`.

Adding a new versioned endpoint means adding a handler to
`api/routes/v0/routes.py` (or a new module under `api/routes/` for a new version)
and registering its router in `api/service.py`.

## Database

The dependency list (`sqlalchemy`, `asyncpg`, `alembic`) and the SQL file under
`migrations/001_create_mock_data.sql` point at a Postgres-backed persistence layer -
a `cars` table with `manufacturers` and `owners` as related tables, pre-seeded with
sample data.

This isn't wired up yet: the Postgres service in `compose.yaml` is commented out, and
no route currently talks to a database. `api/core/` is the intended home for that
code (engine/session setup, models) once it's built out.

## Testing

Tests live under `tests/` and split into two tiers:

- **Unit tests** (`tests/test_api.py`) use FastAPI's `TestClient` to call the app
  in-process, no network or running server required. These run by default.
- **Integration tests** (`tests/test_integration.py`) use a small `requests`-based
  `SessionClient` (`tests/utils/http.py`) to hit a real, running instance of the API
  over HTTP. They're marked `@pytest.mark.integration` and skipped unless
  `--with-integration` is passed, since they require the server to already be up.

Both tiers cover the same behaviors (root, health check, greet success/failure) so
that unit tests can validate application logic quickly while integration tests confirm
the same behavior holds through a real HTTP stack.

## CI

GitHub Actions workflows under `.github/workflows/` handle:

- `pre-commit.yaml` - lint/format checks on every push.
- `testing.yaml` - runs the pytest suite.
- `docs.yaml` - builds this MkDocs site with `mkdocs build --strict` and deploys it to
  GitHub Pages on pushes to `main` that touch `docs/`, `mkdocs.yml`, or
  `pyproject.toml`.
