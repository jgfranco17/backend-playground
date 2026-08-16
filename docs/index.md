# Backend Playground

## Introduction

Backend Playground is a small FastAPI service built as a personal sandbox for backend
development. It exists to give the maintainer (and any other junior/curious engineers
who stumble onto it) a low-stakes place to try out backend tooling end-to-end: a real
API framework, a containerized runtime, database migrations, automated testing, CI, and
this documentation site itself.

There's no product behind this API. The `/v0/greet` endpoint returning a friendly
greeting is intentionally trivial - the point isn't the endpoint, it's everything
wrapped around it.

## Why this project exists

Reading about a tool and wiring it into a working project are different skills. This
repository is a place to close that gap by keeping a full, runnable stack around a
minimal API surface, so that individual pieces (a new middleware, a migration, a CI
step) can be swapped in and tested in isolation without needing to stand up a "real"
production system first.

## What's inside

- **[FastAPI](https://fastapi.tiangolo.com/) service** - a small REST API with a
  versioned route prefix (`/v0`), structured exception handling, and CORS middleware.
- **Docker Compose stack** - the API is containerized and runs via `docker compose up`.
- **Database migrations** - a SQL migration under `migrations/` models a simple
  cars/owners/manufacturers schema, ready to be wired up to a Postgres service.
- **Test suite** - unit tests using FastAPI's `TestClient`, plus opt-in integration
  tests that exercise a running instance of the API over HTTP.
- **CI workflows** - GitHub Actions run pre-commit checks, the test suite, and build
  and deploy this documentation site to GitHub Pages.

## Where to go next

- [Getting Started](getting-started.md) to set up the project and run it locally.
- [API Reference](api-reference.md) for the available endpoints.
- [Architecture](architecture.md) for a tour of the project layout and how the pieces
  fit together.
