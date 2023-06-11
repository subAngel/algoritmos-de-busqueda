class Vertice:
    def __init__(self, i) -> None:
        self.id = i
        self.visitado = False
        self.nivel = -1
        self.padre = None
        self.vecinos = []

    def agregaVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)


class Grafica:
    def __init__(self) -> None:
        self.vertices = {}

    def agregarVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)

    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregaVecino(b)
            self.vertices[b].agregaVecino(b)

    def dfs(self, r):
        if r in self.vertices:
            self.vertices[r].visitados = True

            # recorrer todos los vecinos del nodo r
            for nodo in self.vertices[r].vecinos:
                # ver si el nodo a visitar no ha sido visitado
                if self.vertices[nodo].visitado == False:
                    self.vertices[nodo].padre = r
                    print(f'{str(nodo)}, {str(r)}')
                    self.dfs(nodo)


def main():
    g = Grafica()

    l = [1, 2, 3, 4, 5]
    for v in l:
        g.agregarVertice(v)

    l2 = [1, 2, 1, 5, 2, 3, 2, 5, 3, 4, 4, 6]
    for i in range(0, len(l2)-1, 2):
        g.agregarArista(l2[i], l2[i+1])

    print("(1, Null)")
    g.dfs(1)


main()
