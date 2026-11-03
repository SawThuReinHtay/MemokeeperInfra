from dataclasses import dataclass
from datetime import datetime


@dataclass
class Device:
    device_id: str
    name: str
    device_type: str
    registered_at: datetime
    last_seen: datetime
    online: bool