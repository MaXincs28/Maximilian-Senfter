from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://user:password@localhost/db"
    secret_key: str = "change-me"
    firebase_credentials: str | None = None
    celery_broker_url: str = "redis://localhost:6379/0"
    media_root: str = "media"
    stripe_api_key: str = "sk_test"

    class Config:
        env_file = ".env"

def get_settings() -> Settings:
    return Settings()
