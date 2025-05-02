from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from .database import SessionLocal, init_db
from .crud import (
    create_movie,
    get_movies,
    get_movie_by_id,
    update_movie,
    mark_as_watched,
    delete_movie,
    get_logs
)# Import the CRUD functions
from .schemas import MovieCreate, Movie
from .logger import log_middleware  # Import the logging middleware
from .exceptions import(
    MovieNotFoundException,
    DatabaseException,
    database_exception_handler,
    validation_exception_handler
)
from fastapi.exceptions import RequestValidationError

app = FastAPI()# Initialize FastAPI application

#add exception handlers for database and validation errors
app.add_exception_handler(SQLAlchemyError, database_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# Add the logging middleware to the FastAPI application
app.middleware("http")(log_middleware)

# health check endpoint
@app.get("/health",tags=["Health Check"])
def health_check():
    """
    Health check endpoint to verify if the API is running.
    Returns a simple message indicating the API is up and running.
    """
    return {"status": "healthy", "message": "API is up and running"}

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize the database on startup
# This function is called when the FastAPI application starts up.
@app.on_event("startup")
def startup():
    init_db()


# Add a new movie
@app.post("/movies/", response_model=Movie)
def add_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    try:
        return create_movie(db, movie.name, movie.release_date)
    except SQLAlchemyError as e:
        raise DatabaseException(str(e))


# List all movies
@app.get("/movies/", response_model=list[Movie])
def list_movies(db: Session = Depends(get_db)):
    try:
        movies = get_movies(db)
        if not movies:
            return []
        return movies
    except SQLAlchemyError as e:
        raise DatabaseException(str(e))


# Get movie by ID
@app.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    try:
        movie=get_movie_by_id(db, movie_id)
        if not movie:
            raise MovieNotFoundException()
        return movie
    except SQLAlchemyError as e:
        raise DatabaseException(str(e))


# Update a movie
@app.put("/movies/{movie_id}", response_model=Movie)
def update_movie_details(
    movie_id: int,
    name: str = None,
    release_date: str = None,
    db: Session = Depends(get_db),
):
    try:
        movie = update_movie(db, movie_id, name, release_date)
        if not movie:
            raise MovieNotFoundException()
        return movie
    except SQLAlchemyError as e:
        raise DatabaseException(str(e))


# Mark a movie as watched
@app.put("/movies/{movie_id}/watched", response_model=Movie)
def mark_movie_as_watched(movie_id: int, db: Session = Depends(get_db)):
    try:
        movie = mark_as_watched(db, movie_id)
        if not movie:
            raise MovieNotFoundException()
        return movie
    except SQLAlchemyError as e:
        raise DatabaseException(str(e))


# Soft delete a movie
@app.delete("/movies/{movie_id}")
def soft_delete_movie(movie_id: int, db: Session = Depends(get_db)):
    try:
        movie = delete_movie(db, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        return {"detail": "Movie deleted successfully"}
    except SQLAlchemyError as e:
        raise DatabaseException(str(e))

# Get all logs
@app.get("/logs/", response_model=list[dict])
def list_logs(db: Session = Depends(get_db)):
    """
    Endpoint to retrieve all logs from the database.
    This endpoint returns a list of dictionaries, each containing the method, endpoint, and timestamp of the log entry.
    """
    logs = get_logs(db)
    return logs