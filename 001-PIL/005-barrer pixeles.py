from PIL import Image

imagen = Image.open("josevicente.jpg")
print(imagen)
pixeles = imagen.load()

anchura,altura = imagen.size
for x in range(0,anchura):
    for y in range(0,altura):
        print(pixeles[x,y])
