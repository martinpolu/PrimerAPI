from fastapi import FastAPI,Request,Form
from main import ObtenerPresion, ObtenerTemperatura, ObtenerHumedad
from MongoDB import InsertarTemperatura
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

@app.post("/CargarTemperatura/")
async def login(Temperatura: str = Form(), Ciudad: str = Form(), Horario: str = Form()):
    InsertarTemperatura(Ciudad,Horario,Temperatura)
    return {"Temperatura": Temperatura,"Ciudad": Ciudad,"Horario": Horario}

@app.post("/CargarHumedad/")
async def login(humedad: str = Form(), ciudad: str = Form(), horario: str = Form()):
    return {"Humedad": humedad,"Ciudad": ciudad,"Horario": horario}

@app.post("/CargarPresion/")
async def login(Temperatura: str = Form(), Ciudad: str = Form(), Horario: str = Form()):
    return {"Temperatura": Temperatura,"Ciudad": Ciudad,"Horario": Horario}