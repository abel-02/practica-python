from sqlalchemy import Table, Column, Integer, String
from database import metadata

movies = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("overview", String),
    Column("year", String),
    Column("rating", String),
    Column("category", String)
)
