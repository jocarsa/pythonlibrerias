import os

directorio = "imagenes"

for raiz, directorios, archivos in os.walk(directorio):
    print(archivos)
