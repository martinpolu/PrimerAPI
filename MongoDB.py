from pymongo import MongoClient # import mongo client to connect
import pprint
# Creating instance of mongoclient
client = MongoClient()
# Creating database
def InsertarDato(ciudad,horario,dato,valor):
    db = client.temperatura
    Datos = {"Ciudad": ciudad,
    "Datos": dato,
    "Valor": valor,
    "Horario": horario
    }
    # Creating document
    temperaturas = db.temperatura
    # Inserting data
    temperaturas.insert_one(Datos)
    # Fetching data
    pprint.pprint(temperaturas.find_one())
