from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./local.db"
    secret_key: str = "change-me"
    media_root: str = "media"

    class Config:
        env_file = ".env"

def get_settings() -> Settings:
    return Settings()
