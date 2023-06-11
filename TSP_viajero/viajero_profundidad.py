
matriz_distancias = [[0, 11.85, 6.15, 9.11, 3.13, 5.09, 3.35, 10.60, 7.62, 11.72],
                     [11.85, 0, 9.22, 9.13, 11.93, 11.53, 10.86, 3.89, 10.34, 4.37],
                     [6.15, 9.22, 0, 11.83, 8.62, 9.94, 3.03, 6.23, 11.29, 11.38],
                     [9.11, 9.13, 11.83, 0, 6.77, 4.95, 10.93, 11.16, 2.08, 5.66],
                     [3.13, 11.93, 8.62, 6.77, 0, 2.08, 6.24, 11.7, 4.94, 10.64],
                     [5.09, 11.53, 9.94, 4.95, 2.08, 0, 7.92, 11.98, 2.97, 9.52],
                     [3.35, 10.86, 3.03, 10.93, 6.24, 7.92, 0, 8.62, 9.91, 11.97],
                     [10.60, 3.89, 6.23, 11.16, 11.70, 11.98, 8.62, 0, 11.76, 7.76],
                     [7.62, 10.34, 11.29, 2.08, 4.94, 2.97, 9.91, 11.76, 0, 7.41],
                     [11.72, 4.37, 11.38, 5.66, 10.64, 9.52, 11.97, 7.76, 7.41, 0]
                     ]


def buscar_camino_profundidad(matriz_distancias, ciudad_actual, ciudad_final, profundidad, camino_actual=[]):
    camino_actual.append(ciudad_actual)

    if ciudad_actual == ciudad_final:
        return camino_actual

    if profundidad >= profundidad_maxima:
        camino_actual.pop()
        return None

    for i, distancia in enumerate(matriz_distancias[ciudad_actual]):
        if distancia > 0 and i not in camino_actual:
            camino = buscar_camino_profundidad(matriz_distancias, i, ciudad_final, profundidad + 1, camino_actual)
            if camino:
                return camino

    camino_actual.pop()
    return None


ciudad_inicial = 9
ciudad_destino = 2

profundidad_maxima = 8

camino = buscar_camino_profundidad(matriz_distancias, ciudad_inicial, ciudad_destino, 0)

if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontro un camino")

