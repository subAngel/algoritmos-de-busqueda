from time import time
from collections import  deque
inicio = time()
contador = 0
for i in range(140000):
    contador +=1
fin = time()

print(fin-inicio)

cola = deque([1,2,3,4,5])
cola.append(8)
print(cola)
r = cola.popleft()
print(r)
print(cola)