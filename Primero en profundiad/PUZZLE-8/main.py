from tablero_estados import Tablero_Estados
from tablero import Tablero
estado_inicial = [[8, 7, 2],
                  [1, 3, 6],
                  [4, 0, 5]]
estado_objetivo = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 0]]


arbol = Tablero_Estados(estado_inicial)
arbol.generar_arbol()
arbol.inorden()
