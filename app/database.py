from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Database URL points to SQLite
DATABASE_URL = "sqlite:///./movies.db"

# Create SQLAlchemy engine and sessionmaker
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Initialize the database
def init_db():
    Base.metadata.create_all(bind=engine)
