from PIL import Image

imagen = Image.open("oscuro.jpg")
pixeles = imagen.load()

anchura,altura = imagen.size
max = 0
min = 100000000
for x in range(0,anchura):
    for y in range(0,altura):
        r,v,a = pixeles[x,y]
        luminancia = (r+v+a)/3
        if luminancia > max:
            max = luminancia
        if luminancia < min:
            min = luminancia
print(max,min)
