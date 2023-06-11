from collections import deque


class Nodo:
    def __init__(self, estado):
        self.estado = estado
        self.granjero, self.lobo, self.cabra, self.col = estado

    def __str__(self):
        return f"Granjero: [{self.granjero}], Lobo: [{self.lobo}], Cabra: [{self.cabra}], Col: [{self.col}]"

    def get_sucesores(self):
        sucesores = []
        nuevo_estado = Nodo(('d' if self.granjero == 'i' else 'i', self.lobo, self.cabra, self.col))
        sucesores.append(nuevo_estado)
        # Movimiento del granjero con el lobo
        if self.granjero == self.lobo:
            nuevo_estado = Nodo(('d' if self.granjero == 'i' else 'i',
                                 'd' if self.lobo == 'i' else 'i',
                                 self.cabra,
                                 self.col))
            sucesores.append(nuevo_estado)
            # Movimiento del granjero con la cabra
            if self.granjero == self.cabra:
                nuevo_estado = Nodo(('d' if self.granjero == 'i' else 'i',
                                     self.lobo,
                                     'd' if self.cabra == 'i' else 'i',
                                     self.col))
                sucesores.append(nuevo_estado)
            # Movimiento del granjero con la col
            if self.granjero == self.col:
                nuevo_estado = Nodo(('d' if self.granjero == 'i' else 'i',
                                     self.lobo,
                                     self.cabra,
                                     'd' if self.col == 'i' else 'i'))
                sucesores.append(nuevo_estado)
        return sucesores


def validar_estado(estado):
    granjero, lobo, cabra, col = estado
    if (lobo == cabra and lobo !=granjero) or (cabra==col and cabra!= granjero):
        return False
    return True


# def bfs(estado_inicial, estado_objetivo):
#     visitados = set()
#     cola = deque([[estado_inicial]])
#
#     while cola:
#         camino = cola.popleft()
#         estado_actual = camino[-1]
#         if estado_actual == estado_objetivo:
#             return camino
#         if estado_actual not in visitados and validar_estado(estado_actual):
#             visitados.add(estado_actual)
#             for sucesor in estado_actual.get_sucesores():
#                 if sucesor not in visitados:
#                     nuevo_camino = list(camino)
#                     nuevo_camino.append(sucesor)
#                     cola.append(nuevo_camino)
#     return None

def bfs(nodo_inical, nodo_objetivo):
    visitados = set()
    cola = deque([[nodo_inical]])

    while cola:
        camino = cola.popleft()
        n_actual = camino[-1]

        if n_actual.estado == nodo_objetivo.estado:
            return camino

        if n_actual.estado not in visitados:
            visitados.add(n_actual.estado)
            if validar_estado(n_actual.estado):
                sucesores = n_actual.get_sucesores()
                for sucesor in sucesores:
                    if sucesor.estado not in visitados:
                        nuevo_camino = list(camino)
                        nuevo_camino.append(sucesor)
                        cola.append(nuevo_camino)
    return None




estado_inicial = Nodo(("i", "i", "i", "i"))
estado_objetivo = Nodo(("d", "d", "d", "d"))

solucion = bfs(estado_inicial, estado_objetivo)

if solucion is None:
    print("No se encontro la solucion")
else:
    for estado in solucion:
        print(estado)
