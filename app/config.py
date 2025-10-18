import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_NAME = os.getenv('DB_NAME')
DATABASE_USER = os.getenv('DB_USER')
DATABASE_HOST = os.getenv('DB_HOST')
DATABASE_PASSWORD = os.getenv('DB_PASSWORD')
