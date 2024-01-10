from typing import Union
from fastapi import FastAPI

# Creo la app para despues ejecutar el comando uvicron main:app(depende el nombre de la variable) --reload(Para que se actualice solo cuando haces algun cambio)
app = FastAPI()


# Ruta raiz
@app.get("/")
def read_root():
    return {"Hello": "World!"}

# Ruta ejemplo
@app.get("/saludo")
def hola_mundo():
    return {"Hola": "Mundo"}


@app.get("/items/{item_id}")
def read_iteam(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q} 


@app.get("/calculadora")
def calcular(num1: float, num2: float):
    try:
        return {'suma': num1 + num2}
    except:
        return print("error")

