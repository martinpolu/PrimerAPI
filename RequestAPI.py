import requests
import json
import time
from pymongo import MongoClient
from CodigoCiudades import ListCities
import datetime  

# This script make a request to localhost to obtain values of temp, hum and pres.
# After obtaining them, it uploads them to a database

def ConsultarFechaUltimoDato(CodCity):
    client = MongoClient()
    DataBase = client.clima
    DocClima = DataBase.clima
    result = (DocClima.find({"Ciudad": CodCity}, {}).sort('_id', -1).limit(1)) #Find the last item in db.
    for kas in result:
        print(kas)
        print(datetime.datetime.fromtimestamp( kas["Horario"] )  )
        return(str(kas["Horario"]))
    return 0



while(True):
    for Codigos in ListCities:
        r = requests.get("http://127.0.0.1:50000/Temperatura/?CodCiu="+Codigos)
        res = json.loads(r.text) #Convert text to dict.
        UltimoHorario=ConsultarFechaUltimoDato(Codigos)
        if res["Horario"]!=UltimoHorario:
            datos={'Ciudad':res["Ciudad"],'Dato':'Temperatura','Valor':res["Temperatura"],"Horario":res["Horario"]}
            r = requests.post("http://127.0.0.1:50000/CargarDatos/",data=datos)
            r = requests.get("http://127.0.0.1:50000/Humedad/?CodCiu="+Codigos)
            res = json.loads(r.text)
            datos={'Ciudad':res["Ciudad"],'Dato':'Humedad','Valor':res["Humedad"],"Horario":res["Horario"]}
            r = requests.post("http://127.0.0.1:50000/CargarDatos/",data=datos)
            r = requests.get("http://127.0.0.1:50000/Presion/?CodCiu="+Codigos)
            res = json.loads(r.text)
            datos={'Ciudad':res["Ciudad"],'Dato':'Presion','Valor':res["Presion"],"Horario":res["Horario"]}
            r = requests.post("http://127.0.0.1:50000/CargarDatos/",data=datos)
        else:
            print("mismo dato")
    time.sleep(120)

