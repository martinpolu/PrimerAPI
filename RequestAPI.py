import requests
import json
import time
from pymongo import MongoClient
from CodigoCiudades import ListCities

# This script make a request to localhost to obtain values of temp, hum and pres.
# After obtaining them, it uploads them to a database

def ConsultarFechaUltimoDato():
    client = MongoClient()
    DataBase = client.clima
    DocClima = DataBase.clima
    result=(DocClima.find().sort('_id',-1).limit(1)) #Find the last item in db.
    if result.retrieved==0: #If doesn´t exist values, return 0
        return 0
    else:
        return(result["Horario"])



while(True):
    for Codigos in ListCities:
        r = requests.get("http://127.0.0.1:50000/Temperatura/?CodCiu="+Codigos)
        res = json.loads(r.text) #Convert text to dict.
        UltimoHorario=ConsultarFechaUltimoDato()
        if res["Horario"]!=UltimoHorario:
            datos={'Ciudad':res["Ciudad"],'Dato':'Temperatura','Valor':res["Temperatura"],"Horario":res["Horario"]}
            r = requests.post("http://127.0.0.1:50000/CargarDatos/",data=datos)
            print(r.text)
            r = requests.get("http://127.0.0.1:50000/Humedad/?CodCiu=COR")
            res = json.loads(r.text)
            datos={'Ciudad':res["Ciudad"],'Dato':'Humedad','Valor':res["Humedad"],"Horario":res["Horario"]}
            r = requests.post("http://127.0.0.1:50000/CargarDatos/",data=datos)
            r = requests.get("http://127.0.0.1:50000/Presion/?CodCiu=COR")
            res = json.loads(r.text)
            datos={'Ciudad':res["Ciudad"],'Dato':'Presion','Valor':res["Presion"],"Horario":res["Horario"]}
            r = requests.post("http://127.0.0.1:50000/CargarDatos/",data=datos)
        else:
            print("mismo dato")
    time.sleep(3600)

