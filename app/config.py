import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    SERVER_NAME: str = os.getenv(
        "SERVER_NAME",
        "Memokeeper Infrastructure Server",
    )

    SERVER_ID: str = os.getenv(
        "SERVER_ID",
        "MK-INFRA-DEV-001",
    )

    ENVIRONMENT: str = os.getenv(
        "ENVIRONMENT",
        "development",
    )

    HOST: str = os.getenv(
        "HOST",
        "0.0.0.0",
    )

    PORT: int = int(
        os.getenv(
            "PORT",
            "8000",
        )
    )

    VERSION: str = os.getenv(
        "VERSION",
        "0.1.0",
    )


settings = Settings()