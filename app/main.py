import logging

from fastapi import FastAPI

#for enviroment variables
from app.config import settings
#for logging
from app.logging_config import setup_logging
#for server uptime and status
from app.services.server_status import server_status


setup_logging()

logger = logging.getLogger("memokeeper.infrastructure")


app = FastAPI(
    title="Memokeeper Infrastructure Server",
    version="0.1.0",
)


@app.on_event("startup")
async def startup_event():
    logger.info("Memokeeper Infrastructure Server starting")
    logger.info("Server Name: %s", settings.SERVER_NAME)
    logger.info("Server ID: %s", settings.SERVER_ID)
    logger.info("Environment: %s", settings.ENVIRONMENT)
    logger.info("Version: %s", settings.VERSION)


@app.get("/")
async def root():
    return {
        "server": settings.SERVER_NAME,
        "server_id": settings.SERVER_ID,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "running",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "status": "healthy",
        "server_id": settings.SERVER_ID,
        "version": settings.VERSION,
        **server_status.get_status(),
    }
