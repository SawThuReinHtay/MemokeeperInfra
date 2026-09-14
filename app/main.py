import logging

from fastapi import FastAPI

from app.config import ENVIRONMENT, SERVER_ID, SERVER_NAME
from app.logging_config import setup_logging


setup_logging()

logger = logging.getLogger("memokeeper.infrastructure")


app = FastAPI(
    title="Memokeeper Infrastructure Server",
    version="0.1.0",
)


@app.on_event("startup")
async def startup_event():
    logger.info("Memokeeper Infrastructure Server starting")
    logger.info("Server Name: %s", SERVER_NAME)
    logger.info("Server ID: %s", SERVER_ID)
    logger.info("Environment: %s", ENVIRONMENT)


@app.get("/")
async def root():
    return {
        "server": SERVER_NAME,
        "server_id": SERVER_ID,
        "status": "running",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "server_id": SERVER_ID,
    }