from pymongo import MongoClient # import mongo client to connect
import pprint
# Creating instance of mongoclient
client = MongoClient()
# Creating database
def InsertarTemperatura(ciudad,horario,temperatura):
    db = client.temperatura
    Datos = {"Ciudad": ciudad,
    "Temperatura": temperatura,
    "Horario": horario
    }
    # Creating document
    temperaturas = db.temperatura
    # Inserting data
    temperaturas.insert_one(Datos)
    # Fetching data
    pprint.pprint(temperaturas.find_one())
