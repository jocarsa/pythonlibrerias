import os

directorio = "archivos"

for raiz, directorios, archivos in os.walk(directorio):
    for archivo in archivos:
        ruta = os.path.join(raiz, archivo)
        tamaño = os.path.getsize(ruta)
        print(f"{archivo}: {tamaño} bytes")
