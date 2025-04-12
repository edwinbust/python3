import requests
import json
import arrayPreview

archivo = open("archivo1.txt", "a")

#Fix InsecureRequestWarning
requests.packages.urllib3.disable_warnings()


# Defina la URL de la API de Prometheus
url = 'http://prometheus-k8s-openshift-monitoring.apps.paas-sre.bancogalicia.com.ar/api/v1/query'

# Cargue el archivo de configuración JSON
with open('config.json', 'r') as f:
    config = json.load(f)

# Obtenga el token de autenticación de la cuenta de servicio desde el archivo de configuración
token = config['prometheus_token']


# Defina el encabezado de autorización para incluir el token de autenticación
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

# Defina la consulta que desea realizar
query = '100 - (ceph_cluster_total_bytes-ceph_cluster_total_used_bytes)/ceph_cluster_total_bytes * 100'

# Haga una solicitud HTTP con el encabezado de autorización y la consulta
response = requests.get(url, headers=headers, params={'query': query}, verify=False)

# Verifique si la solicitud fue exitosa
if response.status_code == 200:
    # Imprima la respuesta de la API de Prometheus
    resp = requests.get(url, headers=headers, params={'query': query}, verify=False).text
    data = json.loads(resp)
    value = data['data']['result'][0]['value'][1]
    print (value)
    archivo.write(f"titulo: {value}")
    archivo.write("\n")
    archivo.close()
else:
    # Imprima el código de estado de la respuesta si la solicitud no fue exitosa
    print('Error:', response.status_code)

