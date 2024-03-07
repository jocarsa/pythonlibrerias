from PIL import Image

imagen = Image.open("josevicente.jpg")
print(imagen)
pixeles = imagen.load()
print(pixeles[0,0])

anchura,altura = imagen.size
print(anchura,altura)
