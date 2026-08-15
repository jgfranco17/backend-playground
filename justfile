PORT := "8000"

# List out available commands
_default:
    @just --list --unsorted

# Execute installation
setup:
    @echo "Setting up project..."
    uv sync

# Launch API in debug mode
start:
    @echo "Running main app..."
    uv run uvicorn api.main:app --host 0.0.0.0 --port {{ PORT }} --reload

# Run Pytest unit tests
pytest *args:
	@echo "Running unittest suite..."
	uv run pytest {{ args }}

# Build the API image via Compose
build:
    @echo "Building Docker image..."
    docker compose build api

# Start the full app stack (API + DB) via Compose
up:
    @echo "Starting app stack..."
    docker compose up

# Run the docs server locally
docs:
    mkdocs build --strict --clean
    mkdocs serve --open
