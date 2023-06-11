from collections import deque


class Nodo:
    def __init__(self, estado, padre, profundidad, piezas_correctas) -> None:
        self.estado = estado
        self.padre = padre
        self.profundidad = profundidad
        self.piezas_correctas = piezas_correctas

    def __str__(self) -> str:
        return '\n'.join([' '.join(str(num) for num in row) for row in self.estado])

    def get_sucesores(self):
        sucesores = []
        tablero = self.estado
        filavacia = -1
        columnavacia = -1

        # encontrar el cuadro vacio
        for fila in range(len(tablero)):
            for columna in range(len(tablero[fila])):
                if tablero[fila][columna] == 0:
                    filavacia = fila
                    columnavacia = columna
                    break
        # checar si se puede mover el espacio vacio hacia arriba
        if filavacia > 0:
            estado_copy = [list(fila) for fila in tablero]
            # mover
            estado_copy[filavacia][columnavacia] = estado_copy[filavacia-1][columnavacia]
            estado_copy[filavacia-1][columnavacia] = 0
            sucesores.append(
                Nodo(tuple(map(tuple, estado_copy)), self, self.profundidad+1, calcular_h(estado_copy)))

        # checar si se puede mover hacia abajo
        if filavacia < len(tablero)-1:
            estado_copy = [list(fila) for fila in tablero]

            estado_copy[filavacia][columnavacia] = estado_copy[filavacia+1][columnavacia]
            estado_copy[filavacia+1][columnavacia] = 0

            sucesores.append(
                Nodo(tuple(map(tuple, estado_copy)), self, self.profundidad+1, calcular_h(estado_copy)))

        # checar si se puede mover hacia la derecha
        if columnavacia < len(estado_copy[0]) - 1:
            estado_copy = [list(fila) for fila in tablero]
            estado_copy[filavacia][columnavacia] = estado_copy[filavacia][columnavacia+1]
            estado_copy[filavacia][columnavacia+1] = 0
            sucesores.append(
                Nodo(tuple(map(tuple, estado_copy)), self, self.profundidad+1, calcular_h(estado_copy)))

        # izquierda
        if columnavacia > 0:
            estado_copy = [list(fila) for fila in tablero]

            estado_copy[filavacia][columnavacia] = estado_copy[filavacia][columnavacia-1]
            estado_copy[filavacia][columnavacia-1] = 0
            sucesores.append(
                Nodo(tuple(map(tuple, estado_copy)), self, self.profundidad+1, calcular_h(estado_copy)))

        return sucesores

    def camino(self, inicial):
        camino = []
        nodo_actual = self
        while nodo_actual.profundidad >= 1:
            camino.append(nodo_actual)
            nodo_actual = nodo_actual.padre
        camino.reverse()
        return camino


def calcular_h(estado, objetivo=((1, 2, 3), (4, 5, 6), (7, 8, 0))):
    # valor_correcto = 0
    piezas_correctas = 0
    for i in range(3):
        for j in range(3):
            if estado[i][j] == objetivo[i][j]:
                piezas_correctas += 1
    return piezas_correctas


def busqueda_primero_profundidad(inicial, objetivo, profundidad_max):
    visitados = set()
    frontera = deque()
    nodo_inicial = Nodo(inicial, None, 0, calcular_h(estado_inicial))
    frontera.append(nodo_inicial)

    while frontera:
        nodo = frontera.pop()

        # si el estado del nodo no ha sido visitado
        if nodo.estado not in visitados:
            # ps se visita
            visitados.add(nodo.estado)
        else:
            continue

        if nodo.estado == objetivo:
            print('Solucion')
            return nodo.camino(inicial)
        else:
            if profundidad_max > 0:
                if nodo.profundidad < profundidad_max:
                    frontera.extend(nodo.get_sucesores())
            else:
                frontera.extend(nodo.get_sucesores())


# VARIABLES
limite_profundidad = 100
estado_inicial = ((2, 3, 7), (1, 5, 6), (0, 4, 8))
# estado_inicial = [[2, 3, 7], [1, 0, 5], [6, 4, 8]]
estado_objetivo = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

solucion = busqueda_primero_profundidad(
    estado_inicial, estado_objetivo, limite_profundidad)

if solucion:
    print('se encontro una solucion')
    for nodo in solucion:
        print(nodo)
        print()

else:
    print('no se encontro solucion')
