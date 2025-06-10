# ChatGPT Codex Flask Example

This repository contains a minimal Flask application with a simple health check
and "Hello World" endpoint. The project is ready for test-driven development
and can be run using Docker.

## Project structure

- `app/` - Flask application package
- `tests/` - Pytest test suite
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker image definition

## Running locally

```bash
pip install -r requirements.txt
FLASK_APP=app:create_app flask run
```

## Running with Docker

Build the image and run the container:

```bash
docker build -t chatgpt-codex .
docker run -p 5000:5000 chatgpt-codex
```

Visit `http://localhost:5000` to see the greeting and `http://localhost:5000/health`
for the health check.
