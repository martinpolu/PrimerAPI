import requests
import json


x = requests.get('https://ws.smn.gob.ar/map_items/weather')
# convert dictionary string to dictionary
print(x.text)
res = json.loads(x.text)
