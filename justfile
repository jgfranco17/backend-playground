PROJECT_NAME := "backend-playground"

# List out available commands
_default:
    @just --list

# Execute installation
setup:
    @echo "Setting up project..."
    poetry install

# Launch API in debug mode
start-local:
    @echo "Running main app..."
    poetry run uvicorn api.main:app --host 0.0.0.0 --port 8000

# Start the Docker image
docker-up tag="latest":
    @echo "Starting Docker image..."
    docker build -t {{ PROJECT_NAME }}-api:{{ tag }} -f ./Dockerfile .
    docker run -p 8000:8000 {{ PROJECT_NAME }}-api:{{ tag }}

# Start dev DB
run-db:
    docker compose -f compose.yaml up

# Exec into database image
exec-db database="car_db":
    docker exec -it db-playground psql -U user -d {{ database }}

# Run the docs server locally
docs:
    mkdocs build --strict --clean
    mkdocs serve --open
