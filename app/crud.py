from sqlalchemy.orm import Session
from .models import Movie


def create_movie(db: Session, name: str, release_date: str):
    movie = Movie(name=name, release_date=release_date)
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie


def get_movies(db: Session):
    return db.query(Movie).filter(Movie.status == "active").all()


def get_movie_by_id(db: Session, movie_id: int):
    return (
        db.query(Movie).filter(Movie.id == movie_id, Movie.status == "active").first()
    )


def update_movie(
    db: Session, movie_id: int, name: str = None, release_date: str = None
):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        if name:
            movie.name = name
        if release_date:
            movie.release_date = release_date
        db.commit()
        db.refresh(movie)
    return movie


def mark_as_watched(db: Session, movie_id: int):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        movie.watched = True
        db.commit()
        db.refresh(movie)
    return movie


def delete_movie(db: Session, movie_id: int):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        movie.status = "deleted"
        db.commit()
    return movie
