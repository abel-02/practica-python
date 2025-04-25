from fastapi import FastAPI
from database import metadata, engine
from models import movies

#Nombre app
app = FastAPI()

#Crea tablas automaticamente
metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API conectada a PostgreSQL"}

@app.get("/movies")
def get_movies():
    with engine.connect() as conn:
        result = conn.execute(movies.select()).fetchall()
        return [dict(zip(row._mapping.keys(), row)) for row in result]
