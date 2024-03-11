from PIL import Image
import random
import time

tiempo_inicial = time.time()

imagen = Image.open("josevicente2.jpg")
print(imagen)
pixeles = imagen.load()

altura,anchura = imagen.size
for x in range(0,anchura):
    for y in range(0,altura):
        rojo = pixeles[x,y][0]
        pixeles[x,y] = (rojo,rojo,rojo)
        


tiempo_final = time.time()

print(tiempo_inicial,tiempo_final,(tiempo_final-tiempo_inicial))
imagen.show()
