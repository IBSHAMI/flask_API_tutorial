#!/bin/sh

# Run linting in the Docker container
docker-compose run --rm --entrypoint "" backend sh -c "black app"