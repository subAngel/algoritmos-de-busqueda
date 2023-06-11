from time import time
def es_solucion(estado):
    n = len(estado)
    # si el tablero aun no se llena
    for fila in range(n):
        if estado[fila] == ' ':
            return False
    # verifica por columna
    for i in range(n):
        for j in range(i+1, n):
            if estado[i] == estado[j]:
                return False
    # verifica por diagonal
    for i in range(n):
        for j in range(i+1, n):
            if abs(i-j) == abs(estado[i]-estado[j]):
                return False
    return True


def generar_sucesores(estado):
    n = len(estado)
    sucesores = []
    fila = 0
    for i in range(n):
        if estado[i] != ' ':
            fila += 1
        else:
            break
    # si todas las filas tienen reinas ya no hay sucesores
    if fila == n:
        return sucesores
    # por cada columna se agrega una reina
    for col in range(n):
        nuevo_estado = list(estado)
        nuevo_estado[fila] = col
        sucesores.append(nuevo_estado)
    return sucesores

def resolver(n):
    estado_inicial = [' '] * n
    pila = [estado_inicial]
    # mientras la pila tenga elementos
    while pila:
        estado = pila.pop()
        if es_solucion(estado):
            return estado
        sucesores = generar_sucesores(estado)
        for sucesor in sucesores:
            pila.append(sucesor)
    # No se encontró una solución
    return None


n = 13

t_inicio = time()
solucion = resolver(n)
t_fin = time()

if solucion is not None:
    print("Profundidad")
    print("SOLUCION!!!")
    print(f'{solucion} encontrada en {t_fin-t_inicio}')
    for f in range(len(solucion)):
        fila = ['_'] * n
        fila[solucion[f]] = '*'
        print(' '.join(fila))
else:
    print("No hay solucion")

