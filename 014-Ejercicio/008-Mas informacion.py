import requests
from bs4 import BeautifulSoup
import re
import time

def extraer(url):
    print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    respuesta = requests.get(url, headers=headers)
    xml = BeautifulSoup(respuesta.text, 'html.parser')

    enlaces = xml.find_all(class_="web")
    links = []
    for enlace in enlaces:
        links.append(enlace.get('href'))

    for link in links:
        try:
            print("ok pagina")
            ruta2 = link
            headers2 = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
            }
            respuesta2 = requests.get(ruta2, headers=headers2)
            web = respuesta2.text
            patron = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            resultado = re.findall(patron, web)
            unido = ', '.join(resultado)
            archivo = open("datos.csv",'a')
            archivo.write(link+","+unido+"\n")
            archivo.close()
            time.sleep(1)
        except:
            print("error")
            
    paginacion = xml.find('ul', class_='pagination')  
    elementos = paginacion.find_all('li') 
    ultimo = elementos[-2]
    enlace = ultimo.find('a')
    nuevaruta = enlace['href']
    print("vamos a por la siguiente pagina")
    time.sleep(4)
    extraer(nuevaruta)

extraer("https://www.paginasamarillas.es/a/empresas-de-informatica/madrid/")

