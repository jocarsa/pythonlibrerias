import numpy as np
from PIL import Image
import time

tiempo_inicial = time.time()

imagen = Image.open("josevicente2.jpg")

imagen_array = np.array(imagen)

altura, anchura, _ = imagen_array.shape

grayscale_image = np.mean(imagen_array, axis=2, dtype=np.uint8)

grayscale_pil_image = Image.fromarray(grayscale_image)

tiempo_final = time.time()

print(tiempo_inicial, tiempo_final, (tiempo_final - tiempo_inicial))
grayscale_pil_image.show()
