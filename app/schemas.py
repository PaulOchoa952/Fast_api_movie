from pydantic import BaseModel
from datetime import datetime

class MovieBase(BaseModel):
    name: str
    release_date: str

# This is the MovieCreate model that represents the data for creating a new movie.
class MovieCreate(MovieBase):
    pass

#this is the Movie model that represents the movies table in the database.
class Movie(BaseModel):
    id: int
    name: str
    release_date: str
    watched: bool
    status: str

    class Config:
        from_attributes = True # Enable ORM mode for Pydantic models

# This is the Log model that represents the logs table in the database.
class LogResponse(BaseModel):
    method: str
    endpoint: str
    timestamp: datetime

    class Config:
        from_attributes = True  # Enable ORM mode for Pydantic models