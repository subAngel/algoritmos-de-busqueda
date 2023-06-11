from collections import deque


def validar(fila, columna, reinas):
    for f in range(fila):
        if columna == reinas[f]:
            return False
        elif abs(columna - reinas[f]) == abs(fila - f):
            return False
    return True


# def bfs(fila, reinas, n):
#
#     total_soluciones = 0
#     pos_inicio = (0,0)
#     visitados = set()
#     cola = deque([pos_inicio])
#     while cola:
#         pos_actual = cola.popleft()
#         if pos_actual not in visitados:
#             visitados.add(pos_actual)
#             r, c = pos_actual
#             if r+1 == n:
#                 # se encontro una solucion
#                 print(reinas)
#                 total_soluciones+=1
#                 continue
#
#             if validar(r,c,reinas):
#                 reinas[r] = c
#                 pos_siguientes = [(r+1,col) for col in range(n)]
#                 for siguiente in pos_siguientes:
#                     if len(cola) == 0:
#                         reinas[fila] = ' '
#                         fila -=1
#                     else:
#                         cola.append(siguiente)
#
#
#     return total_soluciones

# def bfs(fila, reinas, n):
#     total_soluciones = 0
#     pos_inicio = (0, 0)
#     visitados = set()
#     cola = deque([pos_inicio])
#     while cola:
#         pos_actual = cola.popleft()
#         if pos_actual not in visitados:
#             visitados.add(pos_actual)
#             r, c = pos_actual
#             siguientes_columnas = [(r, col) for col in range(c, n)]
#             if r + 1 == n:
#                 # se encontro una solucion
#                 print(reinas)
#                 break
#             if validar(r, c, reinas):
#                 reinas[r] = c
#                 siguiente_fila = [(r + 1, col) for col in range(n)]
#                 for siguiente in siguiente_fila:
#                     if len(cola) == 0:
#                         reinas[r] = ' '
#                         r -= 1
#                     else:
#                         cola.append(siguiente)
#     return total_soluciones

def resolver(reinas, n):



def n_reinas(n):
    reinas = [' '] * n # estado inicial
    return resolver(reinas, n)


n_reinas(4)
