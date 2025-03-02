# List out available commands
default:
    @just --list

# Execute installation
setup:
    @echo "Setting up project..."
    poetry install

# Launch API in debug mode
start-local:
    @echo "Running main app..."

# Start the Docker image
docker-up tag="latest":
    @echo "Starting Docker image..."
    docker build -t test-app:{{ tag }} -f ./Dockerfile .
    docker run -p 8000:8000 test-app:{{ tag }}

# Start dev DB
run-db:
    docker compose -f compose.yaml up

# Exec into database image
exec-db database="car_db":
    docker exec -it db-playground psql -U user -d {{ database }}
