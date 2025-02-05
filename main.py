from fastapi import FastAPI, Request
from services.services_m import Servicios
import json

"""
Módulo principal para exponer servicios de cálculo de matrices mediante una API REST.

Este módulo utiliza FastAPI para crear una API que permite calcular la transpuesta de una matriz
a partir de tres vectores proporcionados en formato JSON. Se importan las librerías necesarias
y el módulo de servicios (`Servicios`) para realizar los cálculos.
"""


app = FastAPI()

"""
Se crea una instancia de FastAPI para exponer los servicios.
"""

@app.get("/") # Metadatos o decoradores
def read_root():
    """
    Endpoint raíz que devuelve un mensaje de bienvenida.
    Este endpoint responde a solicitudes GET en la ruta raíz ("/") y devuelve un mensaje
    de bienvenida en formato JSON.
    """
    return {"message": "¡Hola, API!"}

@app.post("/") 
async def read_matriz(request: Request):
    """
    Endpoint para calcular la transpuesta de una matriz a partir de tres vectores.
    
    Este endpoint responde a solicitudes POST en la ruta raíz ("/"). Recibe un cuerpo JSON
    con tres vectores (v1, v2, v3) y utiliza la clase `Servicios` para calcular la transpuesta
    de la matriz formada por estos vectores. La respuesta se devuelve en formato JSON.
    Retorna Una cadena JSON que representa la matriz transpuesta.
    """
    body = await request.json()
    mt = Servicios()
    mtr = mt.calcular_transpuesta(body["v1"], body["v2"], body["v3"])
    return json.dumps(mtr)