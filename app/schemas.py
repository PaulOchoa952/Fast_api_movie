from pydantic import BaseModel
from datetime import datetime

class MovieBase(BaseModel):
    name: str
    release_date: str


class MovieCreate(MovieBase):
    pass


class Movie(BaseModel):
    id: int
    name: str
    release_date: str
    watched: bool
    status: str

    class Config:
        from_attributes = True  # Replace orm_mode with from_attributes

class LogResponse(BaseModel):
    method: str
    endpoint: str
    timestamp: datetime

    class Config:
        from_attributes = True  # Enable ORM mode for Pydantic models