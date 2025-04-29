from fastapi import Request
from datetime import datetime
from sqlalchemy.orm import Session
from .models import Log
from .database import SessionLocal

# Function to log request to the database
def log_to_db(method: str, endpoint: str, db: Session):
    timestamp = datetime.utcnow()
    log_entry = Log(method=method, endpoint=endpoint, timestamp=timestamp)
    db.add(log_entry)
    db.commit()

# Middleware for logging HTTP requests
async def log_middleware(request: Request, call_next):
    # Create a new database session for logging
    db = SessionLocal()
    try:
        # Extract the HTTP method and endpoint path
        method = request.method
        endpoint = request.url.path

        # Log the incoming request into the database
        log_to_db(method, endpoint, db)

        # Proceed with the request
        response = await call_next(request)
        return response
    finally:
        # Close the database session
        db.close()