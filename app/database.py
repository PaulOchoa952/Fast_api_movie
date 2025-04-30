from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

#load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("dotenv module not found. Skipping loading environment variables.")
    raise

# Database URL points to SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./movies.db")

# Create SQLAlchemy engine and sessionmaker
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Initialize the database
def init_db():
    Base.metadata.create_all(bind=engine)
