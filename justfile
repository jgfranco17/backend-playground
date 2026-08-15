PROJECT_NAME := "backend-playground"
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

# Build the Docker image
build tag="latest":
    @echo "Building Docker image..."
    docker build -t {{ PROJECT_NAME }}-api:{{ tag }} -f ./Dockerfile .

# Start the Docker image
up tag="latest":
    @echo "Starting Docker image..."
    docker run -p {{ PORT }}:{{ PORT }} {{ PROJECT_NAME }}-api:{{ tag }}

# Start dev DB
run-db:
    docker compose -f compose.yaml up

# Exec into database image
exec-db database="car_db":
    docker exec -it db-playground psql -U user -d {{ database }} || true

# Run the docs server locally
docs:
    mkdocs build --strict --clean
    mkdocs serve --open
