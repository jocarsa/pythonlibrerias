from PIL import Image
import random

imagen = Image.open("josevicente.jpg")
print(imagen)
pixeles = imagen.load()

altura,anchura = imagen.size
for x in range(0,anchura):
    for y in range(0,altura):
        rojo = pixeles[x,y][0]
        pixeles[x,y] = (rojo,rojo,rojo)
        
imagen.show()
