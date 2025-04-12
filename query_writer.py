import requests
import json

# Cargue el archivo de configuración JSON
with open('config.json', 'r') as f:
    config = json.load(f)
# Imprimir la respuesta del api de prometheus
value = config['data']['result'][0]['value'][1]
print (value)
valor =float(value) 
if valor < 30:
    print("No tenemos advertencia por llenado del storage")
else :
    print("Peligo pasamos en 65%")