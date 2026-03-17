import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "DatabaseUser")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "DatabasePassword")
    DB_NAME = os.getenv("DB_NAME", "dairy_management")
    SECRET_KEY = os.getenv("SECRET_KEY", "dairy_secret_key")
