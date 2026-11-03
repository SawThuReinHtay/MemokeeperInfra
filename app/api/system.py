from fastapi import APIRouter

from app.config import settings
from app.services.server_status import server_status


router = APIRouter(
    prefix="",
    tags=["System"],
)


@router.get("/")
async def root():
    return {
        "server": settings.SERVER_NAME,
        "server_id": settings.SERVER_ID,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "running",
    }


@router.get("/health")
async def health():
    return {
        "server": settings.SERVER_NAME,
        "server_id": settings.SERVER_ID,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        **server_status.get_status(),
    }