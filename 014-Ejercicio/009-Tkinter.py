import requests
from bs4 import BeautifulSoup
import re
import time
import tkinter as tk

def extraer(prefijo,url):
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
            archivo.write(prefijo+","+link+","+unido+"\n")
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


def comienza():
    extraer(prefijo.get(),rutainter.get())


ventana = tk.Tk()

tk.Label(ventana,text="Introduce el prefijo").pack(padx=20,pady=20)
prefijo = tk.Entry(ventana)
prefijo.pack(padx=20,pady=20)

tk.Label(ventana,text="Introduce la url").pack(padx=20,pady=20)
rutainter = tk.Entry(ventana)
rutainter.pack(padx=20,pady=20)

tk.Button(ventana,text="Comenzar",command=comienza).pack(padx=20,pady=20)

ventana.mainloop()
















