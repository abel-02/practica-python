from fastapi import FastAPI

#Nombre app
app = FastAPI()

@app.get("/")
def index():
    return "Hola! Esta es mi primer api en python"