from PIL import Image

imagen = Image.open("josevicente.jpg")
print(imagen)
pixeles = imagen.load()

pixeles[0,0] = (255,255,255)
