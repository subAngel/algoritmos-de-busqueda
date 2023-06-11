class Nodo:
    def __init__(self, tablero) -> None:
        self.tablero = tablero
        self.hijos = []
        # self.izquierda = None
        # self.derecha = None

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def print_nodo(self):
        for fila in self.tablero:
            for columna in fila:
                print(columna, end="\t")
        print()
