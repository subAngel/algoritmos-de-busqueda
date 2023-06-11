from collections import deque
from time import time


def validar(fila, columna, estado):
    # ver si hay una fila en la misma col
    for i in range(fila):
        if estado[i]==columna:
            return False
    # verificar la diagonal
    i = fila - 1
    j = columna - 1
    while i >= 0 and j >= 0:
        if estado[i] == j:
            return False
        i -= 1
        j -= 1
    # Verificar si hay una reina en la otra diagonal
    i = fila - 1
    j = columna + 1
    while i >= 0 and j < n:
        if estado[i] == j:
            return False
        i -= 1
        j += 1
    return True


def es_solucion(estado):
    n = len(estado)
    # Verificar si todas las filas tienen una reina
    for fila in range(n):
        if estado[fila] == ' ':
            return False
    # Verificar si hay dos reinas en la misma columna
    for i in range(n):
        for j in range(i+1, n):
            if estado[i] == estado[j]:
                return False
    # Verificar si hay dos reinas en la misma diagonal
    for i in range(n):
        for j in range(i+1, n):
            if abs(i-j) == abs(estado[i]-estado[j]):
                return False
    return True


def generar_sucesores(estado):
    n = len(estado)
    sucesores = []
    fila = 0
    # si todas las filas ya tienen reinas ya no hay sucesores
    for i in range(n):
        if estado[i] != ' ':
            fila += 1
        else:
            break
    if fila == n:
        return sucesores
    # genera los sucesores
    for col in range(n):
        if validar(fila,col, estado):
            nuevo_estado = list(estado)
            nuevo_estado[fila] = col
            sucesores.append(nuevo_estado)
    return sucesores

def resolver(n):

    estado_inicial = [' '] * n
    cola = deque([estado_inicial])
    while cola:
        estado = cola.popleft()
        if es_solucion(estado):
            return estado
        sucesores = generar_sucesores(estado)
        for sucesor in sucesores:
            cola.append(sucesor)
    # si no hay solucion retorna None
    return None


n = 12
t_inicio = time()
solucion = resolver(n)
t_fin = time()
print("Anchura")
if solucion is not None:
    print("SOLUCION!!!")
    print(f'{solucion} en {t_fin-t_inicio}')
    for f in range(len(solucion)):
        fila = ['_'] * n
        fila[solucion[f]] = '*'
        print(' '.join(fila))
else:
    print("No hay solucion")


# 12 tarda
# 13 tarda 84 seg
