import numpy as np
import time

tiempo_inicial = time.time()

array = np.random.randint(0, 1001, size=10000000)

tiempo_final = time.time()

print(tiempo_inicial, tiempo_final, (tiempo_final - tiempo_inicial))
