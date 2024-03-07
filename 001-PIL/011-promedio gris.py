from PIL import Image
import random

imagen = Image.open("josevicente.jpg")
print(imagen)
pixeles = imagen.load()

altura,anchura = imagen.size
for x in range(0,anchura):
    for y in range(0,altura):
        rojo = pixeles[x,y][0]
        verde = pixeles[x,y][1]
        azul = pixeles[x,y][2]
        promedio = round((rojo+verde+azul)/3)
        pixeles[x,y] = (promedio,promedio,promedio)
        
imagen.show()
