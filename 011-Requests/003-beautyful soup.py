# pip install requests
import requests
# pip install bs4
from bs4 import BeautifulSoup

ruta = "https://jocarsa.com"

respuesta = requests.get(ruta)
xml = BeautifulSoup(respuesta.text, 'html.parser')
print(xml.h3.get_text())
