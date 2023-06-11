# Definir el tablero inicial y el estado objetivo
# None representa el espacio vacío
estado_objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, None]]
tablero_inicial = [[3, 8, 5], [4, 7, 6], [
    2, 1, None]]   # Estado objetivo del juego

# Función para encontrar la posición del espacio vacío


def encontrar_espacio_vacio(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] is None:
                return i, j

# Función para generar los movimientos posibles desde un estado dado


def generar_movimientos(tablero):
    movimientos = []
    fila_vacia, columna_vacia = encontrar_espacio_vacio(tablero)

    # Movimiento hacia arriba
    if fila_vacia > 0:
        nuevo_tablero = [fila.copy() for fila in tablero]
        nuevo_tablero[fila_vacia][columna_vacia], nuevo_tablero[fila_vacia -
                                                                1][columna_vacia] = nuevo_tablero[fila_vacia - 1][columna_vacia], nuevo_tablero[fila_vacia][columna_vacia]
        movimientos.append(nuevo_tablero)

    # Movimiento hacia abajo
    if fila_vacia < len(tablero) - 1:
        nuevo_tablero = [fila.copy() for fila in tablero]
        nuevo_tablero[fila_vacia][columna_vacia], nuevo_tablero[fila_vacia +
                                                                1][columna_vacia] = nuevo_tablero[fila_vacia + 1][columna_vacia], nuevo_tablero[fila_vacia][columna_vacia]
        movimientos.append(nuevo_tablero)

    # Movimiento hacia la izquierda
    if columna_vacia > 0:
        nuevo_tablero = [fila.copy() for fila in tablero]
        nuevo_tablero[fila_vacia][columna_vacia], nuevo_tablero[fila_vacia][columna_vacia -
                                                                            1] = nuevo_tablero[fila_vacia][columna_vacia - 1], nuevo_tablero[fila_vacia][columna_vacia]
        movimientos.append(nuevo_tablero)

    # Movimiento hacia la derecha
    if columna_vacia < len(tablero[0]) - 1:
        nuevo_tablero = [fila.copy() for fila in tablero]
        nuevo_tablero[fila_vacia][columna_vacia], nuevo_tablero[fila_vacia][columna_vacia +
                                                                            1] = nuevo_tablero[fila_vacia][columna_vacia + 1], nuevo_tablero[fila_vacia][columna_vacia]
        movimientos.append(nuevo_tablero)

    return movimientos

# Función de búsqueda primero en profundidad (DFS)


def dfs(tablero_inicial):
    visitados = []
    pila = [(tablero_inicial, [])]

    while pila:
        tablero_actual, ruta = pila.pop()
        visitados.append(tablero_actual)

        if tablero_actual == estado_objetivo:
            return ruta

        movimientos = generar_movimientos(tablero_actual)
        for movimiento in movimientos:
            if movimiento not in visitados:
                nueva_ruta = ruta + [movimiento]
                pila.append((movimiento, nueva_ruta))

    return None


# Llamada inicial al algoritmo DFS
resultado = dfs(tablero_inicial)

# Imprimir el resultado
if resultado is None:
    print("No se encontró solución.")
else:
    print("Se encontró una solución.")
    for tablero in resultado:
        for fila in tablero:
            print(fila)
        print()
