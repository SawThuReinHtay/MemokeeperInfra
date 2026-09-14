import time


class ServerStatus:
    def __init__(self):
        self.start_time = time.time()

    def uptime_seconds(self) -> int:
        return int(time.time() - self.start_time)

    def get_status(self) -> dict:
        return {
            "status": "healthy",
            "uptime_seconds": self.uptime_seconds(),
        }


server_status = ServerStatus()