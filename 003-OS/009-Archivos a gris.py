import os
from PIL import Image

directorio = "imagenes"

for raiz, directorios, archivos in os.walk(directorio):
    for archivo in archivos:
        imagen = Image.open(os.path.join(raiz, archivo))
        pixeles = imagen.load()
        altura,anchura = imagen.size
        for x in range(0,anchura):
            for y in range(0,altura):
                rojo = pixeles[x,y][0]
                pixeles[x,y] = (rojo,rojo,rojo)       
        imagen.save(os.path.join(raiz, archivo))
