from collections import deque
from time import time


def validar(fila, columna, reinas):
    for f in range(fila):
        if columna == reinas[f]:
            # verifica si hay otra reina en la misma columna
            return False
        elif abs(columna - reinas[f]) == abs(fila - f):
            # verifica si hay otra reina en la diagonal
            return False
    return True


def resolver(reinas, n):
    fila = 0
    total_soluciones = 0
    cola = deque([(fila, reinas)])

    while cola:
        fila, reinas = cola.popleft()

        # cuando la fila llegue a la ultima posicion y se agregue uno mas
        # se coloco la ultima reina
        if fila != n:
            # recorremos por anchura (columnas)
            for col in range(n):
                if validar(fila, col, reinas):
                    reinas[fila] = col
                    cola.append((fila + 1, reinas.copy()))
            continue

        for f in range(n):
            fila = ['_'] * n
            fila[reinas[f]] = '*'
            print(' '.join(fila))
        print()

        total_soluciones += 1
        # se salta al siguiente valor en la cola

    return total_soluciones


def n_reinas(n):
    reinas = [' '] * n
    return resolver(reinas, n)


t_inicio = time()
soluciones = n_reinas(8)
t_fin = time()
print(f"Total de soluciones: {soluciones} en {t_fin - t_inicio} sec")
