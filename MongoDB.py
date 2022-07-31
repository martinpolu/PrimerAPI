from pymongo import MongoClient # import mongo client to connect
import json
import pprint

# Creating instance of mongoclient

def InsertarDato(ciudad,horario,dato,valor):
    client = MongoClient()
    DataBase = client.clima
    Datos = {"Ciudad": ciudad, "Datos": dato, "Valor": valor, "Horario": horario}
    DocClima = DataBase.clima
    DocClima.insert_one(Datos)
    result=(DocClima.find().sort('_id',-1).limit(1))
    for j in result:
        print(j)


def ObtTempHistory(ciudad,inicio,fin):
    HistoryValues=[]
    client = MongoClient()
    DataBase = client.clima
    DocClima = DataBase.clima
    result=(DocClima.find({"Ciudad":ciudad, "Datos": "Temperatura"},{"_id":0}))
    for j in result:
        if j["Horario"] > inicio and j["Horario"]<fin :
            HistoryValues.append(j)
    return (HistoryValues)


def ObtHumHistory(ciudad,inicio,fin):
    historyvalues = []
    client = MongoClient()
    DataBase = client.clima
    DocClima = DataBase.clima
    result=(DocClima.find({"Ciudad":ciudad, "Datos": "Humedad"},{"_id":0}))
    for j in result:
        if j["Horario"] > inicio and j["Horario"]<fin :
            historyvalues.append(j)
    return (historyvalues)


def ObtPresHistory(ciudad,inicio,fin):
    HistoryValues=[]
    client = MongoClient()
    DataBase = client.clima
    DocClima = DataBase.clima
    result=(DocClima.find({"Ciudad":ciudad, "Datos": "Presion"},{"_id":0}))
    for j in result:
        if j["Horario"] > inicio and j["Horario"]<fin :
            HistoryValues.append(j)
    return (HistoryValues)