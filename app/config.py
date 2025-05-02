import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """
    Settings class to load environment variables from a .env file.
    """
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        raise ValueError("No DATABASE_URL environment variable found. Please check your .env file")

settings = Settings()