import requests
import json


r = requests.get("http://127.0.0.1:50000/Temperatura/?CodCiu=COR")
res = json.loads(r.text)
datos={'Ciudad':res["Ciudad"],'Dato':'Temperatura','Valor':res["Temperatura"],"Horario":res["Horario"]}
r = requests.post("http://127.0.0.1:50000/CargarDatos/",data=datos)
print(r.text)

