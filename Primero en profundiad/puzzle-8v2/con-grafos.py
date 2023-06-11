

class Edge:
    def __init__(self, nodo1, nodo2):
        self.nodo1 = nodo1  # origen
        self.nodo2 = nodo2  # destino

    def get_nodo1(self):
        return self.nodo1

    def get_nodo2(self):
        return self.nodo2

    def __str__(self):
        return self.nodo1.get_tablero() + "  ----->  " + self.nodo2.get_tablero()


class Nodo:
    def __init__(self, tablero):
        self.tablero = tablero

    def get_tablero(self):
        return self.tablero

    def __str__(self):
        # return '\n'.join([' '.join(str(num) for num in row) for row in self.tablero])
        return self.tablero


class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_node(self, nodo):
        if nodo in self.graph_dict:
            return "El nodo ya existe"
        self.graph_dict[nodo] = []

    def add_arista(self, edge):
        nodo1 = edge.get_nodo1()
        nodo2 = edge.get_nodo2()
        if nodo1 not in self.graph_dict:
            # si el origen no existe
            raise ValueError(
                f'Nodo {nodo1.get_tablero()} no existe en el grafo')
        if nodo2 not in self.graph_dict:
            # si el destino no existe
            raise ValueError(
                f'Nodo {nodo2.get_tablero()} no existe en el grafo')
        self.graph_dict[nodo1].append(nodo2)

    def is_nodo_in(self, nodo):
        return nodo in self.graph_dict

    def get_nodo(self, tablero):
        for n in self.graph_dict:
            if tablero == n.get_tablero():
                return n
        print(f'Nodo {tablero} no existe')
        return None

    def get_neighbors(self, nodo):
        return self.graph_dict[nodo]

    def __str__(self) -> str:
        all_edges = ''
        for n1 in self.graph_dict:
            for n2 in self.graph_dict[n1]:
                all_edges += n1.get_tablero() + '  ---->  ' + n2.get_tablero() + '\n'
        return all_edges


def generar_sucesores(graph, estado_inicial):
    g = graph()
    nodo = g.get_nodo(estado_inicial)
    if nodo is None:
        return

    tablero = nodo.get_tablero()
    f_vacia = -1
    c_vacia = -1

    # encocntrar la pocicion 0(vacia) en el tablero
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if tablero[fila][columna] == 0:
                f_vacia = fila
                c_vacia = columna
                break

    # Izquierda, Derecha, Arriba, Abajo
    direcciones = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    # generar estados nuevos
    for direccion in direcciones:
        nueva_fila = f_vacia + direccion[0]
        nueva_columna = c_vacia + direccion[1]

        if 0 <= nueva_fila < len(tablero) and 0 <= nueva_columna < len(tablero[0]):
            tablero_copia = [fila.copy() for fila in tablero]
            tablero_copia[f_vacia][c_vacia] = tablero_copia[nueva_fila][nueva_columna]
            tablero_copia[nueva_fila][nueva_columna] = 0
            nuevo_nodo = Nodo(tablero_copia)
            g.add_arista(Edge(nodo, nuevo_nodo))
    return g


estado_inicial = [[2, 3, 8],
                  [4, 0, 6],
                  [7, 1, 5]]
grafo = Graph()
G1 = generar_sucesores(Graph, estado_inicial)
print(G1)
