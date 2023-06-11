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

def busqueda_anchura(nodo_inicial, objetivo, limite_profundidad):
   visitados = set()
   #cola de caminos
   cola = deque([nodo_inicial])

   while cola: # mientras haya nodos por explorar
       nodo_actual = cola.popleft() # primer nodo de la cola

       if nodo_actual.estado == objetivo:
           print("Se encontro una solucion")
           return True, len(visitados)
       if nodo_actual.estado not in visitados and nodo_actual.profundidad < limite_profundidad:
           visitados.add(nodo_actual.estado) # se visita
           cola.extend(nodo_actual.get_sucesores()) # se agregan los sucesorea a los nodos por explorar
   print("No se encontro una solucion")
   return False, len(visitados)


tablero_inicial = ((2,4,5),(8,1,3),(0,6,7))
# tablero_inicial = ((1,2,3),(0,5,6),(4,7,8))
# tablero_inicial = ((1, 2, 3), (4, 5, 6), (7, 0, 8))
tablero_objetivo = ((1,2,3),(4,5,6),(7,8,0))
nodo_inicial = Nodo(tablero_inicial, 0)
solucion, total_visitados = busqueda_anchura(nodo_inicial,tablero_objetivo,200)

print(f'Nodos visitados para llegar a la solucion{total_visitados}')



