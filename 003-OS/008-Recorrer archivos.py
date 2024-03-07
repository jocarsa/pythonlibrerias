import os
from PIL import Image

directorio = "imagenes"

for raiz, directorios, archivos in os.walk(directorio):
    for archivo in archivos:
        print(archivo)
