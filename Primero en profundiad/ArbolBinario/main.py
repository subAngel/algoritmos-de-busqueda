from arbol import Arbol

arbol = Arbol("Saige")
arbol.agregar("Arturo")
arbol.agregar("Linnea")
arbol.agregar("Rylee")
arbol.agregar("Tom")
arbol.agregar("Howell")
arbol.agregar("Mitchell")
arbol.agregar("Mandy")
arbol.agregar("Mandy")
arbol.agregar("Erick")

# nombre = input("Ingresa algo para agregar al arbol: ")
# arbol.agregar(nombre)

arbol.inorden()
# arbol.preorden()
# arbol.postorden()

# busqueda
busqueda = input("Busca algo en el arbol: ")
nodo = arbol.buscar(busqueda)
if nodo is None:
    print(f"{busqueda} no existe")
else:
    print(f"{busqueda} si existe")
    # print(nodo.izquierda)
    # print(nodo.dato)
    # print(nodo.derecha)
    # print(arbol.raiz.dato)

arbol2 = Arbol([1, 3, 4])
arbol2.agregar([2, 4, 1])
arbol2.agregar([3, 9, 1])
arbol2.agregar([2, 6, 5])
arbol2.agregar([1, 4, None])
arbol2.agregar([1, 4, 2])


arbol2.inorden()
