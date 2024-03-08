# pip install requests
import requests
# pip install bs4
from bs4 import BeautifulSoup

ruta = "https://jocarsa.com"

respuesta = requests.get(ruta)
xml = BeautifulSoup(respuesta.text, 'html.parser')
titulo = ""
try:
    titulo = xml.title.get_text()
except:
    pass

if titulo == "":
    print("Tu web no tiene titulo, y baja de posicionamiento")
else:
    if len(titulo) < 20:
        print("Tienes un titulo, pero es demasiado corto")
    elif len(titulo) >= 20 and len(titulo) < 100:
        print("Tienes un titulo y es ok")
    elif len(titulo) >= 100:
        print("Tienes un titulo, pero es demasiado largo")
