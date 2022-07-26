from fastapi import FastAPI
from main import ObtenerPresion, ObtenerTemperatura, ObtenerHumedad
app = FastAPI()


@app.get('/Temperatura')
def home():
    return ObtenerTemperatura("COR")

@app.get('/Presion')
def home():
    return ObtenerPresion("COR")

@app.get('/Humedad')
def home():
    return ObtenerHumedad("COR")