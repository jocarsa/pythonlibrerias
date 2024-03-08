
import requests
from bs4 import BeautifulSoup

ruta = "https://www.paginasamarillas.es/a/empresas-de-informatica/valencia/valencia/"

respuesta = requests.get(ruta)
print(respuesta)
xml = BeautifulSoup(respuesta.text, 'html.parser')

enlaces = xml.find_all(class_="web")
print(enlaces)

