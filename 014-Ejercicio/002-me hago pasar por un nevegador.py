
import requests
from bs4 import BeautifulSoup

ruta = "/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
respuesta = requests.get(ruta, headers=headers)
print(respuesta)
xml = BeautifulSoup(respuesta.text, 'html.parser')

enlaces = xml.find_all(class_="web")
print(enlaces)

