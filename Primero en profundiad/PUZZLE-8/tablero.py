class Nodo:
    def __init__(self, estado):
        self.estado = estado
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)


class Tablero:
    def __init__(self, estado_inicial):
        self.raiz = Nodo(estado_inicial)

    def generar_arbol(self, nodo):
        estado_actual = nodo.estado
        movimientos = self.generar_movimientos(estado_actual)

        for movimiento in movimientos:
            nuevo_nodo = Nodo(movimiento)
            nodo.agregar_hijo(nuevo_nodo)
            self.generar_arbol(nuevo_nodo)

    def generar_movimientos(self, estado):
        movimientos = []

        # Generar movimientos para cada posición del tablero
        for i in range(len(estado)):
            for j in range(len(estado[i])):
                # Realizar movimientos posibles para cada posición

                # Movimiento hacia arriba
                if i > 0:
                    nuevo_estado = self.realizar_movimiento(
                        estado, i, j, i-1, j)
                    movimientos.append(nuevo_estado)

                # Movimiento hacia abajo
                if i < len(estado) - 1:
                    nuevo_estado = self.realizar_movimiento(
                        estado, i, j, i+1, j)
                    movimientos.append(nuevo_estado)

                # Movimiento hacia la izquierda
                if j > 0:
                    nuevo_estado = self.realizar_movimiento(
                        estado, i, j, i, j-1)
                    movimientos.append(nuevo_estado)

                # Movimiento hacia la derecha
                if j < len(estado[i]) - 1:
                    nuevo_estado = self.realizar_movimiento(
                        estado, i, j, i, j+1)
                    movimientos.append(nuevo_estado)

        return movimientos

    def realizar_movimiento(self, estado, fila_origen, columna_origen, fila_destino, columna_destino):
        # Realizar el movimiento en el estado actual
        nuevo_estado = [fila.copy() for fila in estado]
        nuevo_estado[fila_origen][columna_origen], nuevo_estado[fila_destino][columna_destino] = nuevo_estado[
            fila_destino][columna_destino], nuevo_estado[fila_origen][columna_origen]
        return nuevo_estado

    def generar_arbol_completo(self):
        self.generar_arbol(self.raiz)
