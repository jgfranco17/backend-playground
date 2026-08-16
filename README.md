# Backend Playground

## Overview

A playground for backend development things. Intended to be a personal reference and for playing
with various backend developer tools in a repeatable way.

## Getting Started

To get started with this project, follow the steps below.

### Prerequisites

Ensure you have the following installed on your machine:

- [Python 3.13](https://www.python.org/downloads/release/python-3130/) or above
- [Docker](https://docs.docker.com/engine/install/)
- [UV](https://docs.astral.sh/uv/getting-started/) for package management

### Setup

1. Clone the repository and navigate into the project directory.

   ```bash
   git clone https://github.com/jgfranco17/backend-playground.git
   cd backend-playground
   ```

2. Install the required dependencies using UV.

   ```bash
   uv sync
   ```

3. To start the development server locally, we use Uvicorn as the
   ASGI server to run the FastAPI application.

   ```bash
   # Run with UV directly
   uv run uvicorn api.main:app --port <port>

   # Or use the provided Just command for convenience
   just start
   ```

## Testing

This project uses [`pytest`](https://docs.pytest.org/en/stable/how-to/usage.html) for
testing. Test cases are defined in `tests` directory.
