from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/api_movies"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
