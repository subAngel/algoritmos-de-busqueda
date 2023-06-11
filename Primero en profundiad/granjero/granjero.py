class Estado:
    def __init__(self, granjero, lobo, cabra, col):
        self.granjero = granjero
        self.lobo = lobo
        self.cabra = cabra
        self.col = col

    def __str__(self):
        return f"Granjero: {self.granjero}, Lobo: {self.lobo}, Cabra: {self.cabra}, Col: {self.col}"

    def get_sucesores(self):  # acciones
        sucesores = []
        # movimiento del granjero
        # el granjero pasa solo
        nuevo_estado = Estado('derecha' if self.granjero == 'izquierda' else 'izquierda',
                              self.lobo,
                              self.cabra,
                              self.col)
        sucesores.append(nuevo_estado)
        # el granjero pasa con el lobo
        if self.granjero == self.lobo:
            nuevo_estado = Estado('derecha' if self.granjero == 'izquierda' else 'izquierda',
                                  'derecha' if self.lobo == 'izquierda' else 'izquierda',
                                  self.cabra,
                                  self.col)
            sucesores.append(nuevo_estado)
        # el granjero pasa con la cabra
        if self.granjero == self.cabra:
            nuevo_estado = Estado('derecha' if self.granjero == 'izquierda' else 'izquierda',
                                  self.lobo,
                                  'derecha' if self.cabra == 'izquierda' else 'izquierda',
                                  self.col)
            sucesores.append(nuevo_estado)
        # el granjero pasa con la col
        if self.granjero == self.col:
            nuevo_estado = Estado('derecha' if self.granjero == 'izquierda' else 'izquierda',
                                  self.lobo, self.cabra,
                                  'derecha' if self.col == 'izquierda' else 'izquierda')
            sucesores.append(nuevo_estado)
        return sucesores


def validar_estado(estado: Estado):
    if (estado.lobo == estado.cabra and estado.lobo != estado.granjero) or (
            estado.cabra == estado.col and estado.cabra != estado.granjero):
        return False
    return True


def dfs_granjero(estado_actual, estado_final, visitados, ruta):
    if estado_actual == estado_final:
        ruta.append(estado_actual)  # Agregar estado actual a la ruta
        return True

    visitados.add(estado_actual)  # Marcar el estado actual como visitado

    for sucesor in estado_actual.get_sucesores():
        if sucesor not in visitados:  # Evitar ciclos
            if validar_estado(sucesor):  # Verificar si el estado es válido
                if dfs_granjero(sucesor, estado_final, visitados, ruta):
                    ruta.append(estado_actual)  # Agregar estado actual a la ruta
                    return True

    return False


def dfs_w_pila(estado, estado_objetivo, ruta):

    ruta.append(estado)
    if estado == estado_objetivo:
        return ruta

    vecinos = estado.get_sucesores()
    for v in vecinos:
        if v not in ruta:
            if validar_estado(v):
                new_path = dfs_w_pila(v, estado_objetivo, ruta)
                if new_path is not None:
                    return new_path


estado_inicial = Estado("izquierda", "izquierda", "izquierda", "izquierda")
estado_final = Estado("derecha", "derecha", "derecha", "derecha")

solucion = dfs_w_pila(estado_inicial, estado_final, [])

for n in solucion:
    print(n)