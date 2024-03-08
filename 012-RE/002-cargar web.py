import re
import requests

ruta = "https://escuelamastermedia.es/"
respuesta = requests.get(ruta)
web = respuesta.text

patron = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

resultado = re.findall(patron, web)
print(resultado)
