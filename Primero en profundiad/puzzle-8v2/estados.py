from collections import deque
class Nodo:
    def __init__(self, estado, profundidad) -> None:
        self.estado = estado
        self.profundidad = profundidad

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
                Nodo(tuple(map(tuple, estado_copy)), self.profundidad+1))

        # checar si se puede mover hacia abajo
        if filavacia < len(tablero)-1:
            estado_copy = [list(fila) for fila in tablero]

            estado_copy[filavacia][columnavacia] = estado_copy[filavacia+1][columnavacia]
            estado_copy[filavacia+1][columnavacia] = 0

            sucesores.append(
                Nodo(tuple(map(tuple, estado_copy)), self.profundidad+1))

        # checar si se puede mover hacia la derecha
        if columnavacia < len(estado_copy[0]) - 1:
            estado_copy = [list(fila) for fila in tablero]
            estado_copy[filavacia][columnavacia] = estado_copy[filavacia][columnavacia+1]
            estado_copy[filavacia][columnavacia+1] = 0
            sucesores.append(
                Nodo(tuple(map(tuple, estado_copy)), self.profundidad+1))

        # izquierda
        if columnavacia > 0:
            estado_copy = [list(fila) for fila in tablero]

            estado_copy[filavacia][columnavacia] = estado_copy[filavacia][columnavacia-1]
            estado_copy[filavacia][columnavacia-1] = 0
            sucesores.append(
                Nodo(tuple(map(tuple, estado_copy)), self.profundidad+1))

        return sucesores


def dfs(nodo, objetivo, visitados, limite_profundidad):

    if nodo.estado == objetivo:
        return True

    visitados.add(nodo.estado)

    if nodo.profundidad < limite_profundidad:
        for sucesor in nodo.get_sucesores():
            if sucesor.estado not in visitados:
                # dfs(sucesor, objetivo, visitados, limite_profundidad, contador)
                if dfs(sucesor, objetivo, visitados, limite_profundidad):
                    return True
    # si no ha encontrado una solucion retorna false
    return False



limite_profundidad = 100
estado_inicial = ((2, 3, 7), (1, 5, 6), (0, 4, 8))
# estado_inicial = ((8, 1, 3), (4, 0, 6), (5, 7,2))
# estado_inicial = ((8, 1, 3), (4, 0, 6), (5, 7,2))

# estado_inicial = ((7, 5, 1), (0, 2, 8), (3, 6, 4))
estado_inicial = ((1, 2, 3), (4, 5, 6), (7, 0, 8))
# estado_inicial = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
estado_objetivo = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
nodo_inicial = Nodo(estado_inicial, 0)
dfs = dfs(nodo_inicial, estado_objetivo, set(),limite_profundidad)

print("Solucion encontrada" if dfs else "No hay solucion")
# if dfs:
#     print("Solucion encontrada")
# else:
#     print("No se encontro la solucion")

