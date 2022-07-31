Infoclima API

Desde hace algunos años, me pareció importante registrar los datos del clima para hacer análisis con estos datos y poder analizar relaciones entre humedad, temperatura y presión. 
Hace algunos meses comence a introducirme en el mundo de python, a partir de esto, decidí crear una "API" bastante básica pero que fuese útil para poder registrar los datos de temperatura. 
Así se armó esta idea. 
El proyecto consta con un web server, en mi caso utilizo uvicorn para poder montarlo. Este genera los endpoints necesarios para funcionar:



/Temperatura/?CodCiu= -> Este endpoint permite obtener la temperatura actual de un sitio, este dato debe enviarse como parámetro. Para simplicar se lo debe enviar con un cierto formato. 

  "COR" -> Córdoba 
  "BUE" -> Buenos Aires
  "SJ" -> San Juan
  "SL" -> San Luis
  "MDQ -> Mar del Plata
  
  Ej: /Temperatura/?CodCiu=COR

  Respuesta esperada: Codigo de la ciudad para control, valor de la temperatura en ºC, horario informado del dato en epoch.
  
  Ej:
  {
      "Ciudad": "COR", 
      "Temperatura": 18.2,
      "Horario": "1659222000"
  }


/Humedad/?CodCiu= -> Este endpoint permite obtener la humedad actual de un sitio, el dato del lugar de consultad debe enviarse como parámetro. 
  
  
  Respuesta esperada: Codigo de la ciudad para control, valor de la humedad como %, horario informado del dato en epoch.
  
  Ej: /Humedad/?CodCiu=COR

  Respuesta esperada:
  
  
  {
      "Ciudad": "COR",
      "Humedad": 36.0,
      "Horario": "1659222000"
  }
 
 
/Presion/?CodCiu= -> Este endpoint permite obtener la presion actual de un sitio, el dato del lugar de consultad debe enviarse como parámetro. 
  
  Ej: /Presion/?CodCiu=COR

  Respuesta esperada:
  
  
  Respuesta esperada: Codigo de la ciudad para control, valor de la presión en hPa, horario informado del dato en epoch.
  
  {
    "Ciudad": "COR",
    "Presion": 962.8,
    "Horario": "1659222000"
}

/CargarDatos/ -> Este endpoint permite cargar los datos en una base de datos basada en mongo, la misma se genera en otro script (también creado en el proyecto). Para cargarlos se utiliza el método POST. Debe enviarse los parámetros para cargar.
Ciudad: Codigo de la ciudad
Dato: Temperatura, Humedad o Presion
Valor: Valor del dato
Horario: Hora informada del dato en formato epoch

Body:

datos={'Ciudad':"COR",'Dato':'Temperatura','Valor':12.12,"Horario":12354}


/TemperaturaHistorico/?CodCiu=&FechaInicio=&FechaFin= -> Este endpoint permite consultar el valor de temperatura para un sitio, utilizando los códigos nombrados anteriormente, desde una fecha de comienzo hasta una fecha de fin (informando el fechas con formato epoch). 

Ej:

/TemperaturaHistorico/?CodCiu=COR&FechaInicio=0&FechaFin=1659225742

Respuesta esperada:

[
    {
        "Ciudad": "COR",
        "Datos": "Temperatura",
        "Valor": 15.1,
        "Horario": 1658872800
    },
    {
        "Ciudad": "COR",
        "Datos": "Temperatura",
        "Valor": 19.2,
        "Horario": 1659132000
    }
]

            
