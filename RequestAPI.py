import requests
import json
r = requests.get("http://127.0.0.1:50000/Temperatura/?CodCiu=COR")
res = json.loads(r.text)
print(res)
r = requests.post("http://127.0.0.1:50000/CargarTemperatura",data=res)
print(r.text)