from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.device_service import device_service


router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
)


class DeviceRegistrationRequest(BaseModel):
    device_id: str
    name: str
    device_type: str


@router.post("/register")
async def register_device(request: DeviceRegistrationRequest):

    if device_service.device_exists(request.device_id):
        raise HTTPException(
            status_code=409,
            detail="Device already registered",
        )

    device = device_service.register_device(
        device_id=request.device_id,
        name=request.name,
        device_type=request.device_type,
    )

    return {
        "message": "Device registered successfully",
        "device": {
            "device_id": device.device_id,
            "name": device.name,
            "device_type": device.device_type,
            "registered_at": device.registered_at,
            "last_seen": device.last_seen,
            "online": device.online,
        },
    }


@router.post("/{device_id}/heartbeat")
async def heartbeat(device_id: str):

    device = device_service.heartbeat(device_id)

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return {
        "message": "Heartbeat received",
        "device_id": device.device_id,
        "last_seen": device.last_seen,
        "online": device.online,
    }

@router.get("/{device_id}")
async def get_device(device_id: str):

    device = device_service.get_device(device_id)

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return {
        "device_id": device.device_id,
        "name": device.name,
        "device_type": device.device_type,
        "registered_at": device.registered_at,
        "last_seen": device.last_seen,
        "online": device.online,
    }