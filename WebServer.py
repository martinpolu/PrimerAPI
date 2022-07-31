from fastapi import FastAPI,Request,Form
from main import ObtenerPresion, ObtenerTemperatura, ObtenerHumedad
from MongoDB import InsertarDato,ObtTempHistory,ObtHumHistory,ObtPresHistory
app = FastAPI()


@app.get('/Temperatura/')
async def LecturaTemperatura(CodCiu: str):
    return ObtenerTemperatura(CodCiu)

@app.get('/Presion/')
async def LecturaPresion(CodCiu: str):
    return ObtenerPresion(CodCiu)

@app.get('/Humedad/')
async def LecturaHumedad(CodCiu: str):
    return ObtenerHumedad(CodCiu)

@app.post("/CargarDatos/")
async def CargarDatos(Valor: float = Form(), Ciudad: str = Form(), Horario: int = Form(), Dato: str = Form()):
    InsertarDato(Ciudad,Horario,Dato,Valor)
    return {"Dato": Dato,"Ciudad": Ciudad,"Horario": Horario,"Valor":Valor}

@app.get('/TemperaturaHistorico/')
async def TempHistory(CodCiu: str, FechaInicio: int, FechaFin : int):
    return ObtTempHistory(CodCiu,FechaInicio,FechaFin)

@app.get('/HumedadHistorico/')
async def HumHistory(CodCiu: str, FechaInicio: int, FechaFin : int):
    return ObtHumHistory(CodCiu,FechaInicio,FechaFin)

@app.get('/PresionHistorico/')
async def PresHistory(CodCiu: str, FechaInicio: int, FechaFin : int):
    return ObtPresHistory(CodCiu,FechaInicio,FechaFin)
