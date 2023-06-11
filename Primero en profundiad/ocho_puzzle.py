#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ocho_puzzle.py
------------

Ejemplo del problema del Ocho puzzle resuelto con diferentes métodos de búsqueda


"""

__author__ = 'juliowaissman'


import busquedas


class Ocho_puzzle(busquedas.ProblemaBusqueda):
    """
    El problema del 8 puzzle.

    El estado es una lista de 10 números, donde el 0 es
    el espacio vacío. Por ejemplo el estado:

           (1, 0, 2, 3, 4, 5, 6, 7, 8, pos0)

    representa la situación:
       -------------
       | 1 |   | 2 |
       -------------
       | 3 | 4 | 5 |
       -------------
       | 6 | 7 | 8 |
       ------------

    Las acciones posibles son A = {N,S,E,O}

    """

    def __init__(self, pos_ini):
        """
        Inicializa un diccionario de acciones legales para ahorrar tiempo

        """
        super(Ocho_puzzle, self).__init__(pos_ini + (pos_ini.index(0),), lambda s: s == (0, 1, 2, 3, 4, 5, 6, 7, 8, 0))

        self.acciones = {0: ['S', 'E'],
                         1: ['S', 'E', 'O'],
                         2: ['S', 'O'],
                         3: ['N', 'S', 'E'],
                         4: ['N', 'S', 'E', 'O'],
                         5: ['N', 'S', 'O'],
                         6: ['N', 'E'],
                         7: ['N', 'E', 'O'],
                         8: ['N', 'O']}

    def acciones_legales(self, estado):

        return self.acciones[estado[-1]]

    def sucesor(self, estado, accion):

        s = list(estado)
        ind = s[-1]
        if accion == 'N':
            s[ind], s[ind - 3], s[-1] = s[ind - 3], s[ind], ind - 3
        elif accion == 'S':
            s[ind], s[ind + 3], s[-1] = s[ind + 3], s[ind], ind + 3
        elif accion == 'O':
            s[ind], s[ind - 1], s[-1] = s[ind - 1], s[ind], ind - 1
        elif accion == 'E':
            s[ind], s[ind + 1], s[-1] = s[ind + 1], s[ind], ind + 1
        return tuple(s)

    @staticmethod
    def dibuja(estado):
        """
        Dibuja un estado particular

        """
        cadena = "-------------\n"
        for i in range(3):
            for j in range(3):
                if estado[3 * i + j] > 0:
                    cadena += "| " + str(estado[3 * i + j]) + " "
                else:
                    cadena += "|   "
            cadena += "|\n-------------\n"
        return cadena


def prueba_busqueda(pos_inicial, metodo, heuristica=None, max_prof=None):
    """
    Prueba un método de búsqueda para el problema del 8 puzzle.

    @param pos_inicial: Una tupla con una posicion inicial (una tupla con 8 valores)
    @param metodo: Un metodo de búsqueda a probar
    @param heuristica: Una función de heurística, por default None si el método de búsqueda no requiere heuristica
    @param max_prof: Máxima profundidad para los algoritmos de DFS y IDS.

    @return nodo: El nodo solución

    """
    if heuristica:
        return metodo(Ocho_puzzle(pos_inicial), heuristica)
    elif max_prof:
        return metodo(Ocho_puzzle(pos_inicial), max_prof)
    else:
        return metodo(Ocho_puzzle(pos_inicial))


if __name__ == "__main__":

    def h_1(nodo):
        "Regresa el número de piezas mal colocadas"
        return sum([1 for i in range(1, 9) if i != nodo.estado[i]])

    def h_2(nodo):
        "Regresa la suma de las distancias de manhattan de los numeros mal colocados"
        return sum([abs(i % 3 - nodo.estado[i] % 3) + abs(i // 3 - nodo.estado[i] // 3)
                    for i in range(9) if nodo.estado[i] != 0])

    def h_3(nodo):
        return max(h_1(nodo), h_2(nodo))

    pos_ini = (1, 0, 2, 3, 4, 5, 6, 7, 8)
    print "Vamos a ver como funciona la UCS con un problema de 8 puzzle"
    print "\n" + Ocho_puzzle.dibuja(pos_ini)
    #n = prueba_busqueda(pos_ini, busquedas.busqueda_costo_uniforme)
    n = prueba_busqueda(pos_ini, busquedas.busqueda_A_estrella, h_3)
    print "\n\n", "-" * 30 + '\n', n
    print "Explorando ", n.nodos_visitados, " nodos"

    pos_ini = (5, 1, 3, 4, 0, 2, 6, 7, 8)
    print "\n\n\n" + '-'*30 + '\n'
    print "y con otro problema de 8 puzzle"
    print "\n" + Ocho_puzzle.dibuja(pos_ini)
    #n = prueba_busqueda(pos_ini, busquedas.busqueda_costo_uniforme)
    n = prueba_busqueda(pos_ini, busquedas.busqueda_A_estrella, h_3)
    print "\n\n", "-" * 30 + '\n', n
    print "Explorando ", n.nodos_visitados, " nodos"

    pos_ini = (1, 7, 8, 2, 3, 4, 5, 6, 0)
    print "\n\n\n" + '-'*30 + '\n'
    print "y por último"
    print "\n" + Ocho_puzzle.dibuja(pos_ini)
    #n = prueba_busqueda(pos_ini, busquedas.busqueda_costo_uniforme)
    n = prueba_busqueda(pos_ini, busquedas.busqueda_A_estrella, h_3)
    print "\n\n", "-" * 30 + '\n', n
    print "Explorando ", n.nodos_visitados, " nodos"
