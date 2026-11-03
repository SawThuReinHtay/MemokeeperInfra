import logging

from fastapi import FastAPI

from app.api.system import router as system_router
from app.api.devices import router as devices_router
from app.config import settings
from app.logging_config import setup_logging


setup_logging()

logger = logging.getLogger("memokeeper.infrastructure")


app = FastAPI(
    title="Memokeeper Infrastructure Server",
    version=settings.VERSION,
)


app.include_router(system_router)
app.include_router(devices_router)


@app.on_event("startup")
async def startup_event():
    logger.info("Memokeeper Infrastructure Server starting")
    logger.info("Server Name: %s", settings.SERVER_NAME)
    logger.info("Server ID: %s", settings.SERVER_ID)
    logger.info("Environment: %s", settings.ENVIRONMENT)
    logger.info("Version: %s", settings.VERSION)