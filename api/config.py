import os

from dotenv import load_dotenv


def _getenv(key, default=None) -> str:
    value = os.environ.get(key, default)
    if value is None:
        raise NameError(f'Environment key "{key}" not found, recheck your .env file.')
    return value


load_dotenv()


class Config:
    """Service configurations"""

    APP_TITLE = _getenv("APP_TITLE", "NASA judge")
    APP_DESCRIPTION = _getenv("APP_DESCRIPTION", "Docker judge for NCKU NASA course")
    VERSION = _getenv("VERSION", "0.0.0")
    OPENAPI_URL = _getenv("OPENAPI_URL", "/openapi.json")

    DB_URL = _getenv("DB_URL", "postgresql://postgres:password@localhost:5432/database")
