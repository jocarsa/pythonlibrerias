import time
import random

tiempo_inicial = time.time()

lista = []

for i in range(0,10000000):
    lista.append(random.randint(0,1000))

tiempo_final = time.time()

print(tiempo_inicial,tiempo_final,(tiempo_final-tiempo_inicial))
