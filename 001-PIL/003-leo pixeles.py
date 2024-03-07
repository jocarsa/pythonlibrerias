from PIL import Image

imagen = Image.open("josevicente.jpg")
print(imagen)
pixeles = imagen.load()
print(pixeles[0,0])

