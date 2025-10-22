import os
import pytz
from dotenv import load_dotenv
from functools import lru_cache
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "Azeem Blog"
    admin_email: str
    database_name: str
    database_user: str
    database_password: str
    database_host: str
    secret_key: str
    allowed_hosts: list = ["*"]
    debug: bool

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

indian_timezone = pytz.timezone('Asia/Kolkata')


