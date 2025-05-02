from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
import logging

#configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class MovieNotFoundException(HTTPException):
    """
    Exception raised when a movie is not found in the database.
    Inherits from HTTPException and sets the status code to 404 (Not Found).
    """
    def __init__(self):
        super().__init__(status_code=404, detail="movie not found")

class DatabaseException(HTTPException):
    """
    Exception raised for database-related errors.
    Inherits from HTTPException and sets the status code to 500 (Internal Server Error).
    """
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=detail)
        logger.error(f"Database error: {detail}")

async def database_exception_handler(request: Request, exc: SQLAlchemyError):
    """
    Custom exception handler for SQLAlchemy errors.
    Logs the error and returns a JSON response with a 500 status code.
    """
    logger.error(f"Database error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"},
    )

async def validation_exception_handler(request: Request, exc: Exception):
    """
    Custom exception handler for validation errors.
    Logs the error and returns a JSON response with a 400 status code.
    """
    return JSONResponse(
        status_code=400,
        content={"detail": "Invalid request data"},
    )