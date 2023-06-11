class Directed_Graph:
    def __init__(self):
        self.graph_dictionary = {}

    def add_node(self, nodo):
        if nodo in self.graph_dictionary:
            return "Nodo already in graph"
        self.graph_dictionary[nodo] = []

    def add_edge(self, edge):
        nodo1 = edge.get_nodo1()
        nodo2 = edge.get_nodo2()
        if nodo1 not in self.graph_dictionary:
            # si el origen no existe
            raise ValueError(f'Nodo {nodo1.get_name()} not in graph')
        if nodo2 not in self.graph_dictionary:
            raise ValueError(f'Nodo {nodo2.get_name()} not in graph')
        self.graph_dictionary[nodo1].append(nodo2)

    def is_nodo_in(self, nodo):
        return nodo in self.graph_dictionary

    def get_nodo(self, nodo_name):
        for n in self.graph_dictionary:
            if nodo_name == n.get_name():
                return n
        print(f'Nodo {nodo_name} does not exists')

    def get_neighbors(self, nodo):
        return self.graph_dictionary[nodo]

    def __str__(self):
        all_edges = ''
        for n1 in self.graph_dictionary:
            for n2 in self.graph_dictionary[n1]:
                all_edges += n1.get_name() + '  ----->  ' + n2.get_name() + '\n'
        return all_edges


class Edge:
    def __init__(self, nodo1, nodo2):
        self.nodo1 = nodo1  # origen
        self.nodo2 = nodo2  # destino

    def get_nodo1(self):
        return self.nodo1

    def get_nodo2(self):
        return self.nodo2

    def __str__(self):
        return self.nodo1.get_name() + "  ----->  " + self.nodo2.get_name()


class Nodo:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Undirected_Graph(Directed_Graph):
    def add_edge(self, edge):
        Directed_Graph.add_edge(self, edge)
        edge_back = Edge(edge.get_nodo2(), edge.get_nodo1())
        Directed_Graph.add_edge(self, edge_back)


def build_graph(graph):
    g = graph()
    for n in ("s", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'x'):
        g.add_node(Nodo(n))
    g.add_edge(Edge(g.get_nodo('s'), g.get_nodo('a')))
    g.add_edge(Edge(g.get_nodo('s'), g.get_nodo('b')))
    g.add_edge(Edge(g.get_nodo('s'), g.get_nodo('c')))
    g.add_edge(Edge(g.get_nodo('s'), g.get_nodo('d')))
    g.add_edge(Edge(g.get_nodo('a'), g.get_nodo('b')))
    g.add_edge(Edge(g.get_nodo('a'), g.get_nodo('g')))
    g.add_edge(Edge(g.get_nodo('d'), g.get_nodo('c')))
    g.add_edge(Edge(g.get_nodo('d'), g.get_nodo('f')))
    # g.add_edge(Edge(g.get_nodo('d'), g.get_nodo('e')))

    return g


G1 = build_graph(Undirected_Graph)
print(G1)
