from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://user:password@localhost/db"
    secret_key: str = "change-me"

    class Config:
        env_file = ".env"

def get_settings() -> Settings:
    return Settings()
