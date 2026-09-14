import os

from dotenv import load_dotenv

load_dotenv()


SERVER_NAME = os.getenv(
    "SERVER_NAME",
    "Memokeeper Infrastructure Server"
)

SERVER_ID = os.getenv(
    "SERVER_ID",
    "MK-INFRA-DEV-001"
)

ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    "development"
)