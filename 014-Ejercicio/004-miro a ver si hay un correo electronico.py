import requests
from bs4 import BeautifulSoup
import re
import time

ruta = "https://www.paginasamarillas.es/a/empresas-de-informatica/valencia/valencia/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
respuesta = requests.get(ruta, headers=headers)
xml = BeautifulSoup(respuesta.text, 'html.parser')

enlaces = xml.find_all(class_="web")
links = []
for enlace in enlaces:
    links.append(enlace.get('href'))
print(links)

for link in links:
    ruta2 = link
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    respuesta2 = requests.get(ruta2, headers=headers2)
    web = respuesta2.text
    patron = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    resultado = re.findall(patron, web)
    print(link,resultado)
    time.sleep(1)
