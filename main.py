"""Minimal, isolated FastAPI health-check service for the DigitalOcean pilot."""

from fastapi import FastAPI

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}
