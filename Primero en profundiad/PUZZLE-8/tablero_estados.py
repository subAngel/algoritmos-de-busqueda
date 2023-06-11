from nodo import Nodo

# Arbol de los estados del tablero


class Tablero_Estados:
    def __init__(self, tablero) -> None:
        self.raiz = Nodo(tablero)

    def __inorden_recursivo(self,  nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo)
            self.__inorden_recursivo(nodo.derecha)

    def __generar_movimientos(self, tablero):
        movimientos = []
        f_vacia = -1  # fila vacia
        c_vacia = -1  # columna vacia

        # encontrar el cuadro vacio
        for fila in range(len(tablero)):
            for columna in range(len(tablero[fila])):
                if tablero[fila][columna] is 0:
                    f_vacia = fila
                    c_vacia = columna
                    break

        # checar si se puede mover el espacio vacio hacia arriba
        if f_vacia > 0:
            tablero_copy = [fila.copy() for fila in tablero]
            # mover
            tablero_copy[f_vacia][c_vacia] = tablero_copy[f_vacia-1][c_vacia]
            tablero_copy[f_vacia-1][c_vacia] = 0
            movimientos.append(tablero_copy)

        # checar si se puede mover hacia abajo
        if f_vacia < len(tablero)-1:
            tablero_copy = [fila.copy() for fila in tablero]

            tablero_copy[f_vacia][c_vacia] = tablero_copy[f_vacia+1][c_vacia]
            tablero_copy[f_vacia+1][c_vacia] = 0

            movimientos.append(tablero_copy)

        # checar si se puede mover hacia la derecha
        if c_vacia < len(tablero_copy[0]) - 1:
            tablero_copy = [fila.copy() for fila in tablero]
            tablero_copy[f_vacia][c_vacia] = tablero_copy[f_vacia][c_vacia+1]
            tablero_copy[f_vacia][c_vacia+1] = 0
            movimientos.append(tablero_copy)

        # izquierda
        if c_vacia > 0:
            tablero_copy = [fila.copy() for fila in tablero]

            tablero_copy[f_vacia][c_vacia] = tablero_copy[f_vacia][c_vacia-1]
            tablero_copy[f_vacia][c_vacia-1] = 0
            movimientos.append(tablero_copy)

        return movimientos

    def __agregar_recursivo(self, nodo, tablero):
        if tablero < nodo.tablero:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(tablero)
            else:
                self.__agregar_recursivo(nodo.izquierda, tablero)
        elif tablero > nodo.tablero:
            if nodo.derecha is None:
                nodo.derecha = Nodo(tablero)
            else:
                self.__agregar_recursivo(nodo.derecha, tablero)

    def inorden(self):
        print("Imprimiendo argol inorden:")
        self.__inorden_recursivo(self.raiz)
        print("")

    def agregar(self, tablero):
        self.__agregar_recursivo(self.raiz, tablero)

    def generar_arbol(self):
        movimientos = self.__generar_movimientos(self.raiz.tablero)
        for mov in movimientos:
            self.agregar(mov)
