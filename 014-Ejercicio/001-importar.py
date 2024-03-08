
import requests
from bs4 import BeautifulSoup

ruta = ""

respuesta = requests.get(ruta)
print(respuesta)
xml = BeautifulSoup(respuesta.text, 'html.parser')

enlaces = xml.find_all(class_="web")
print(enlaces)

