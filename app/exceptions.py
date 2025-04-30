from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
import logging

#configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class MovieNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="movie not found")

class DatabaseException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=detail)
        logger.error(f"Database error: {detail}")

async def database_exception_handler(request: Request, exc: SQLAlchemyError):
    logger.error(f"Database error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"},
    )

async def validation_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={"detail": "Invalid request data"},
    )