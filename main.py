import requests
import datetime
from bs4 import BeautifulSoup
from CodigoCiudades import Ciudades


def ObtenerTemperatura(Ciudad):
    x = requests.get(Ciudades[Ciudad])
    #print(x.text)
    soup = BeautifulSoup(x.text, "html.parser")
    TablaTemperatura = soup.find_all("div", {"class": "d1"})
    Temperatura=TablaTemperatura[1].text.split()[0][:-2] #Obtenemos temperatura sacandole el "ºC"
    TablaRegistro = soup.find_all("div",{"class":"nota1 ea"})
    HoraRegistro=int(TablaRegistro[0].text.split()[3])
    if datetime.datetime.now().hour>HoraRegistro:#Verificamos si la hora es del día anterior.
        FechaRegistro=datetime.datetime.now()
        FechaRegistro=FechaRegistro.replace(hour=HoraRegistro, minute=0, second=0, microsecond=0)
    else:
        FechaRegistro=datetime.datetime.now() + datetime.timedelta(days=-1)
        FechaRegistro=FechaRegistro.replace(hour=HoraRegistro, minute=0, second=0, microsecond=0)
    return({"Ciudad":Ciudad,"Temperatura":Temperatura,"Horario":FechaRegistro})

def ObtenerHumedad(Ciudad):
    x = requests.get(Ciudades[Ciudad])
    #print(x.text)
    soup = BeautifulSoup(x.text, "html.parser")
    TablaHumedad = soup.find_all("div", {"class": "d1"})
    Humedad=TablaHumedad[2].text.split()[1][:-1] #Obtenemos presion sacandole el "%"
    TablaRegistro = soup.find_all("div",{"class":"nota1 ea"})
    HoraRegistro=int(TablaRegistro[0].text.split()[3])
    if datetime.datetime.now().hour>HoraRegistro: #Verificamos si la hora es del día anterior.
        FechaRegistro=datetime.datetime.now()
        FechaRegistro=FechaRegistro.replace(hour=HoraRegistro, minute=0, second=0, microsecond=0)
    else:
        FechaRegistro=datetime.datetime.now() + datetime.timedelta(days=-1)
        FechaRegistro=FechaRegistro.replace(hour=HoraRegistro, minute=0, second=0, microsecond=0)
    return({"Ciudad":Ciudad,"Humedad":Humedad,"Horario":FechaRegistro})

def ObtenerPresion(Ciudad):
    x = requests.get(Ciudades[Ciudad]) #Hacemos el get para obtener el json completo
    #print(x.text)
    soup = BeautifulSoup(x.text, "html.parser")
    TablaPresion = soup.find_all("div", {"class": "d1"})
    Presion=TablaPresion[2].text.split()[3] #Obtenemos temperatura sacandole el "ºC"
    TablaRegistro = soup.find_all("div",{"class":"nota1 ea"})
    HoraRegistro=int(TablaRegistro[0].text.split()[3])
    if datetime.datetime.now().hour>HoraRegistro: #Verificamos si la hora es del día anterior.
        FechaRegistro=datetime.datetime.now()
        FechaRegistro=FechaRegistro.replace(hour=HoraRegistro, minute=0, second=0, microsecond=0)
    else:
        FechaRegistro=datetime.datetime.now() + datetime.timedelta(days=-1)
        FechaRegistro=FechaRegistro.replace(hour=HoraRegistro, minute=0, second=0, microsecond=0)

    return({"Ciudad":Ciudad,"Presion":Presion,"Horario":FechaRegistro})

