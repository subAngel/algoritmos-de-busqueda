

def validar(fila, columna, reinas):
    for f in range(fila):
        if columna == reinas[f]:
            return False
        # ya hay una dama atacando en diagonal
        elif abs(columna - reinas[f]) == abs(fila - f): return False
    return True


def place_queen(reinas, n):
    fila = 0
    total_soluciones = 0
    pila = [(fila, reinas)]

    while pila:
        fila, reinas = pila.pop()
        if fila == n:
            for f in range(n):
                fila = ['_']*n
                fila[reinas[f]] = '*'
                print(' '.join(fila))
            print()

            total_soluciones += 1
            continue

        for col in range(n):
            if validar(fila, col, reinas):
                reinas[fila] = col
                pila.append((fila + 1, reinas.copy()))

    return total_soluciones


def n_queens(n):
    queens = [' ']*n
    return place_queen(queens, n)

soluciones = n_queens(4)
print(f"Total de soluciones: {soluciones}")