import requests
import json
from bs4 import BeautifulSoup
from CodigoCiudades import Ciudades


def ObtenerTemperatura(Ciudad):
    x = requests.get(Ciudad) #Hacemos el get para obtener el json completo
    #print(x.text)
    soup = BeautifulSoup(x.text, "html.parser")
    TablaTemperatura = soup.find_all("div", {"class": "d1"})
    Temperatura=TablaTemperatura[1].text.split()[0][:-2] #Obtenemos temperatura sacandole el "ºC"
    TablaRegistro = soup.find_all("div",{"class":"nota1 ea"})
    HoraRegistro=(TablaRegistro[0].text.split()[3])
    return({"Temperatura":Temperatura,"Horario":HoraRegistro})

def ObtenerHumedad(Ciudad):
    x = requests.get(Ciudad) #Hacemos el get para obtener el json completo
    #print(x.text)
    soup = BeautifulSoup(x.text, "html.parser")
    TablaHumedad = soup.find_all("div", {"class": "d1"})
    Humedad=TablaHumedad[2].text.split()[1][:-1] #Obtenemos presion sacandole el "%"
    TablaRegistro = soup.find_all("div",{"class":"nota1 ea"})
    HoraRegistro=(TablaRegistro[0].text.split()[3])
    return({"Humedad":Humedad,"Horario":HoraRegistro})

def ObtenerPresion(Ciudad):
    x = requests.get(Ciudad) #Hacemos el get para obtener el json completo
    #print(x.text)
    soup = BeautifulSoup(x.text, "html.parser")
    TablaPresion = soup.find_all("div", {"class": "d1"})
    Presion=TablaPresion[2].text.split()[3] #Obtenemos temperatura sacandole el "ºC"
    TablaRegistro = soup.find_all("div",{"class":"nota1 ea"})
    HoraRegistro=(TablaRegistro[0].text.split()[3])
    return({"Presion":Presion,"Horario":HoraRegistro})



print(ObtenerPresion(Ciudades["MDQ"]))
print(ObtenerTemperatura(Ciudades["MDQ"]))
print(ObtenerHumedad(Ciudades["MDQ"]))