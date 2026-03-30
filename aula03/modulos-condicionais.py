import math

num = 17
raiz = math.sqrt(num)
print(f"A raiz de {num} é {raiz: .2f}")

graus = 60
radiano = graus / 180 * math.pi
seno = math.sin(radiano)

print("\n", seno)

import random

num_random = random.random()
print(num_random) #jamais vai sortear o 1
print(num_random*10) #se quiser um número de 0 a 10, sem ser o 10 jamais

num_rand_int = random.randint(1, 10)
print(num_rand_int)