from datetime import datetime, timezone

from app.models import device
from app.models.device import Device


class DeviceService:
    def __init__(self):
        self.devices: dict[str, Device] = {}

    def register_device(
        self,
        device_id: str,
        name: str,
        device_type: str,
    ) -> Device:

        now = datetime.now(timezone.utc)

        device = Device(
            device_id=device_id,
            name=name,
            device_type=device_type,
            registered_at=now,
            last_seen=now,
            online=True,
        )

        self.devices[device_id] = device

        return device

    def get_device(self, device_id: str) -> Device | None:
        device = self.devices.get(device_id)

        if device is None:
            return None

        elapsed = (
            datetime.now(timezone.utc) - device.last_seen
        ).total_seconds()

        device.online = elapsed < 60

        return device

    def device_exists(self, device_id: str) -> bool:
        return device_id in self.devices

    def heartbeat(self, device_id: str) -> Device | None:
        device = self.devices.get(device_id)

        if device is None:
            return None

        device.last_seen = datetime.now(timezone.utc)
        device.online = True

        return device

device_service = DeviceService()