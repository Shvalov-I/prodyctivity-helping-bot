from sqlalchemy import URL, create_engine

from app.config import app_settings

_db_url = URL.create(
    drivername="postgresql",
    username=app_settings.DB_USERNAME,
    password=app_settings.DB_PASSWORD,
    host=app_settings.DB_HOST,
    port=app_settings.DB_PORT,
    database=app_settings.DB_NAME,
)

ENGINE = create_engine(url=_db_url)
