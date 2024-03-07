import os

directorio = os.getcwd()
archivo = "josevicente.jpg"
ruta = os.path.join(directorio, archivo)

soloarchivo = os.path.basename(ruta)
print(soloarchivo)
