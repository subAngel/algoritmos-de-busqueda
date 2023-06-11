# Definir el tablero inicial
# None representa el espacio vacío
tablero = [[1, 2, 3], [4, 5, 6], [7, 8, None]]

# Función para imprimir el tablero


def imprimir_tablero(tablero):
    for fila in tablero:
        for elemento in fila:
            if elemento is None:
                print(" ", end="\t")
            else:
                print(elemento, end="\t")
        print()

# Función para verificar si el jugador ha ganado


def verificar_ganador(tablero):
    numeros_correctos = 0
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == i*len(tablero) + j + 1:
                numeros_correctos += 1
    return numeros_correctos == len(tablero) * len(tablero[0]) - 1

# Función para mover una pieza en el tablero


def mover_pieza(tablero, fila, columna):
    # Verificar si el movimiento es válido
    if fila < 0 or fila >= len(tablero) or columna < 0 or columna >= len(tablero[0]):
        print("Movimiento inválido. Intente nuevamente.")
        return

    # Verificar si la casilla seleccionada está vacía
    if tablero[fila][columna] is None:
        print("Casilla vacía. Intente nuevamente.")
        return

    # Verificar si se puede mover la pieza hacia el espacio vacío
    fila_vacia, columna_vacia = encontrar_espacio_vacio(tablero)
    if (fila != fila_vacia and columna != columna_vacia) or (fila == fila_vacia and columna == columna_vacia):
        print("Movimiento inválido. Intente nuevamente.")
        return

    # Realizar el movimiento
    tablero[fila_vacia][columna_vacia], tablero[fila][columna] = tablero[fila][columna], tablero[fila_vacia][columna_vacia]

# Función para encontrar la posición del espacio vacío


def encontrar_espacio_vacio(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] is None:
                return i, j


# Juego principal
while not verificar_ganador(tablero):
    imprimir_tablero(tablero)

    fila = int(input("Ingrese la fila de la pieza que desea mover: "))
    columna = int(input("Ingrese la columna de la pieza que desea mover: "))

    mover_pieza(tablero, fila, columna)

print("¡Felicidades! Has ganado el juego.")
