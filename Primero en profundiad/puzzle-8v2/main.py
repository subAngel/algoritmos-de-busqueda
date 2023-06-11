class Nodo:
    def __init__(self, tablero):
        self.tablero = tablero
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def get_hijos(self):
        for hijo in self.hijos:
            hijo.imprimir_nodo()

    def imprimir_nodo(self):
        for fila in self.tablero:
            for columna in fila:
                print(columna, end="\t")
            print()


class Arbol:
    def __init__(self, estado_inicial) -> None:
        self.raiz = Nodo(estado_inicial)

    def agregar_nodo(self, nodo_padre, nuevo_nodo):
        nodo_padre.agregar_hijo(nuevo_nodo)

    def __inorden_recursivo(self):
        pass

    def __generar_movimientos(self, tablero):
        movimientos = []
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
            tablero_copy = [fila.copy() for fila in tablero]
            # mover
            tablero_copy[filavacia][columnavacia] = tablero_copy[filavacia-1][columnavacia]
            tablero_copy[filavacia-1][columnavacia] = 0
            movimientos.append(tablero_copy)

        # checar si se puede mover hacia abajo
        if filavacia < len(tablero)-1:
            tablero_copy = [fila.copy() for fila in tablero]

            tablero_copy[filavacia][columnavacia] = tablero_copy[filavacia+1][columnavacia]
            tablero_copy[filavacia+1][columnavacia] = 0

            movimientos.append(tablero_copy)

        # checar si se puede mover hacia la derecha
        if columnavacia < len(tablero_copy[0]) - 1:
            tablero_copy = [fila.copy() for fila in tablero]
            tablero_copy[filavacia][columnavacia] = tablero_copy[filavacia][columnavacia+1]
            tablero_copy[filavacia][columnavacia+1] = 0
            movimientos.append(tablero_copy)

        # izquierda
        if columnavacia > 0:
            tablero_copy = [fila.copy() for fila in tablero]

            tablero_copy[filavacia][columnavacia] = tablero_copy[filavacia][columnavacia-1]
            tablero_copy[filavacia][columnavacia-1] = 0
            movimientos.append(tablero_copy)

        return movimientos

    def __generar_arbol_recursivo(self, nodo, visitados):
        tablero_actual = nodo.tablero
        movimientos = self.__generar_movimientos(tablero_actual)

        for mov in movimientos:
            if mov not in visitados:
                visitados.append(mov)
                nuevo_nodo = Nodo(mov)
                nodo.agregar_hijo(nuevo_nodo)
                self.__generar_arbol_recursivo(nuevo_nodo, visitados)

    def generar_arbol(self):
        visitados = [self.raiz.tablero]
        self.__generar_arbol_recursivo(self.raiz, visitados)


estado_inicial = [[2, 3, 7], [1, 5, 6], [0, 4, 8]]
arbol = Arbol(estado_inicial)

sucesores = arbol.__generar_movimientos(estado_inicial)
print(sucesores)
