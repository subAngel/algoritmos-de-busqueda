from collections import deque
import time


class TableroState:
    def __init__(self, tablero):
        self.estado = tablero

    def __str__(self):
        return str(self.estado)
        # return '\n'.join([' '.join(str(num) for num in row) for row in self.estado])

    def __eq__(self, other):
        return self.estado == other.estado

    def __hash__(self):
        return hash(str(self.estado))

    def get_sucesores(self):
        sucesores = []
        tablero = self.estado

        fila_vacia = -1
        columna_vacia = -1
        tablero_copy = [fila.copy() for fila in tablero]

        for fila in range(len(tablero_copy)):
            for columna in range(len(tablero_copy[fila])):
                if tablero_copy[fila][columna] == 0:
                    fila_vacia = fila
                    columna_vacia = columna
                    break

        # Checar si se puede mover el espacio vacío hacia arriba
        if fila_vacia > 0:
            tablero_copy[fila_vacia][columna_vacia] = tablero_copy[fila_vacia-1][columna_vacia]
            tablero_copy[fila_vacia-1][columna_vacia] = 0
            sucesores.append(TableroState(tablero_copy))

        # Checar si se puede mover hacia abajo
        if fila_vacia < len(tablero_copy)-1:
            tablero_copy = [fila.copy() for fila in tablero]
            tablero_copy[fila_vacia][columna_vacia] = tablero_copy[fila_vacia+1][columna_vacia]
            tablero_copy[fila_vacia+1][columna_vacia] = 0
            sucesores.append(TableroState(tablero_copy))

        # Checar si se puede mover hacia la derecha
        if columna_vacia < len(tablero_copy[0]) - 1:
            tablero_copy = [fila.copy() for fila in tablero]
            tablero_copy[fila_vacia][columna_vacia] = tablero_copy[fila_vacia][columna_vacia+1]
            tablero_copy[fila_vacia][columna_vacia+1] = 0
            sucesores.append(TableroState(tablero_copy))

        # Checar si se puede mover hacia la izquierda
        if columna_vacia > 0:
            tablero_copy = [fila.copy() for fila in tablero]
            tablero_copy[fila_vacia][columna_vacia] = tablero_copy[fila_vacia][columna_vacia-1]
            tablero_copy[fila_vacia][columna_vacia-1] = 0
            sucesores.append(TableroState(tablero_copy))

        return sucesores


def resolver(inicio, objetivo):
    pila = deque([inicio])
    visitados = set([inicio])
    movimientos = {inicio: []}

    while len(pila) > 0:
        estado_actual = pila.pop()

        if estado_actual == objetivo:
            for movimiento in movimientos[estado_actual]:
                print(f'{movimiento[0]} --> {movimiento[1]}')
            return

        sucesores = estado_actual.get_sucesores()

        for sucesor in sucesores:
            if sucesor not in visitados:
                pila.append(sucesor)
                visitados.add(sucesor)
                movimientos[sucesor] = movimientos[estado_actual] + \
                    [(estado_actual, sucesor)]

    return None


tab_inicial = [[2, 3, 7], [1, 8, 4], [6, 5, 0]]
# tab_inicial = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
# [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
tab_objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

estado_inicial = TableroState(tab_inicial)
estado_objetivo = TableroState(tab_objetivo)

resolver(estado_inicial, estado_objetivo)
