import os
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional, List

class Settings(BaseSettings):
    version: str = "0.2.0"
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./prism_workforce.db")
    nova_database_url: str = os.getenv("NOVA_DATABASE_URL", "sqlite:///../NOVA/nova_finance.db")
    openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
    anthropic_api_key: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    debug: bool = Field(default=False)
    port: int = 8004
    cors_origins: List[str] = ["http://localhost:8004", "http://127.0.0.1:8004"]

    class Config:
        env_file = ".env"

settings = Settings()
