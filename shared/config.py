from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    api_token: str
    database_url: str


def get_settings() -> Settings:
    token = getenv("API_TOKEN", "").strip()

    if not token:
        raise RuntimeError("API_TOKEN is not set. Create .env from .env.example.")

    return Settings(
        api_token=token,
        database_url=getenv("DATABASE_URL", "sqlite+aiosqlite:///./demo_orders.db"),
    )
