import requests
import datetime
import re
from bs4 import BeautifulSoup
from CodigoCiudades import ListCities


def ObtenerTemperatura(Ciudad):
    result=None
    while result is None:
        try:
            x = requests.get(ListCities[Ciudad])
            soup = BeautifulSoup(x.text, "html.parser")
            TablaDatos = soup.find_all("div", {"class": "nota1 ea"})
            texto=(TablaDatos[0].text) #Find text with temp,hum and pres.
            Temperatura=(re.findall("^[-0-9.]+°C", texto, re.MULTILINE))
            Temperatura=float(Temperatura[0][:-2])
            HoraRegistro=int(re.findall("[0-9]+.?(?= hs)", texto, re.MULTILINE)[0])
            if datetime.datetime.now().hour>=HoraRegistro: #Check if values it´s from today.
                FechaRegistro=datetime.datetime.now()
                FechaRegistro=FechaRegistro.replace(hour=HoraRegistro, minute=0, second=0, microsecond=0)
            else:
                FechaRegistro=datetime.datetime.now() + datetime.timedelta(days=-1)
                FechaRegistro=FechaRegistro.replace(hour=HoraRegistro, minute=0, second=0, microsecond=0)
            result= {"Ciudad":Ciudad,"Temperatura":Temperatura,"Horario":FechaRegistro.strftime("%s")}
            return(result)
        except Exception as ex:
            print(ex)
            pass


def ObtenerHumedad(Ciudad):
    result=None
    while result is None:
        try:
            x = requests.get(ListCities[Ciudad])
            soup = BeautifulSoup(x.text, "html.parser")
            TablaDatos = soup.find_all("div",{"class":"nota1 ea"})
            texto=(TablaDatos[0].text) #Find text with temp,hum and pres.
            Humedad=float(re.findall("(?<=Humedad: ).[0-9]", texto, re.MULTILINE)[0])
            HoraRegistro=int(re.findall("[0-9]+.?(?= hs)", texto, re.MULTILINE)[0])
            if datetime.datetime.now().hour>=HoraRegistro: #Check if values it´s from today.
                FechaRegistro=datetime.datetime.now()
                FechaRegistro=FechaRegistro.replace(hour=HoraRegistro, minute=0, second=0, microsecond=0)
            else:
                FechaRegistro=datetime.datetime.now() + datetime.timedelta(days=-1)
                FechaRegistro=FechaRegistro.replace(hour=HoraRegistro, minute=0, second=0, microsecond=0)
            result= {"Ciudad":Ciudad,"Humedad":Humedad,"Horario":FechaRegistro.strftime("%s")}
            return(result)
        except:
            pass


def ObtenerPresion(Ciudad):
    result=None
    while result is None:
        try:
            x = requests.get(ListCities[Ciudad]) #Find text with temp,hum and pres.
            soup = BeautifulSoup(x.text, "html.parser")
            TablaDatos = soup.find_all("div",{"class":"nota1 ea"})
            texto = (TablaDatos[0].text)
            Presion = float(re.findall("(?<=Presión: ).[0-9.]+", texto, re.MULTILINE)[0])
            HoraRegistro = int(re.findall("[0-9]+.?(?= hs)", texto, re.MULTILINE)[0])
            if datetime.datetime.now().hour>=HoraRegistro: #Check if values it´s from today.
                FechaRegistro=datetime.datetime.now()
                FechaRegistro=FechaRegistro.replace(hour=HoraRegistro, minute=0, second=0, microsecond=0)
            else:
                FechaRegistro=datetime.datetime.now() + datetime.timedelta(days=-1)
                FechaRegistro=FechaRegistro.replace(hour=HoraRegistro, minute=0, second=0, microsecond=0)
            result= {"Ciudad":Ciudad,"Presion":Presion,"Horario":FechaRegistro.strftime("%s")}
            return(result)
        except:
            pass
