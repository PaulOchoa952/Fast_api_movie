from pydantic import BaseModel


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
