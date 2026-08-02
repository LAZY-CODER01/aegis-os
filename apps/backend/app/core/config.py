from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    APP_NAME: str = "Aegis OS"

    VERSION: str = "0.0.1"

    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()