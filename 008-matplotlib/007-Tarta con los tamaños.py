import os
import matplotlib.pyplot as plt

directorio = "archivos"

tamaños = []
nombres = []

for raiz, directorios, archivos in os.walk(directorio):
    for archivo in archivos:
        ruta = os.path.join(raiz, archivo)
        nombres.append(ruta)
        tamaños.append(os.path.getsize(ruta))

plt.pie(tamaños, labels=nombres, autopct='%1.1f%%')

plt.show()
