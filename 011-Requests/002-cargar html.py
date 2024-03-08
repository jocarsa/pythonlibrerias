# pip install requests
import requests

ruta = "https://jocarsa.com"

respuesta = requests.get(ruta)
print(respuesta.text)
