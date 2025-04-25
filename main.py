from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import HTMLResponse

#Nombre app
app = FastAPI()


@app.get("/")
def index():
    return "Hola a as"    #Automaticamente lo convierte en json
"""
class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional [str]

@app.get("/libros/{id}")
def mostrarLibro(id: int): #Podemos convertir a entero en vez de str
    return {"data" : id}

@app.post("/libros")
def insertarLibro(libro: Libro):
    return {"message" : f"libro {libro.titulo} insertado"}
"""

movies = [
    {
        "id":1,
        "title": "Avatar",
        "overview": "En un exuberante plantea llama...",
        "year":"2009",
        "rating": 7.8,
        "category": "Accion"
    }
]

def buscarPelicula(id):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return "Película no encontrada"



#Mostrar elementos de html
@app.get("/h")
def saludo():
    return HTMLResponse('<h1>Hola <h1>')

@app.get("/movies")
def getPeliculas():
    return movies

@app.get("/movies/{id}")
def getPeliculas(id: int):
    return buscarPelicula(id)