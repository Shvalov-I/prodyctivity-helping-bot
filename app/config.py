from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class AppSettings(BaseSettings):
    DB_NAME: str = "prodyctivity_bot"
    DB_USERNAME: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432


app_settings = AppSettings()
