from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World!"}


@app.get("/saludo")
def hola_mundo():
    return {"Hola": "Mundo"}