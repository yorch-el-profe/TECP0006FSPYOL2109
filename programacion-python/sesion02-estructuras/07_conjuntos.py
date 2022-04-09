"""
Conjuntos:
Son una colección de elementos, que no se repiten y no tienen un orden

Sintaxis:
conjunto_vacio = set()
conjunto = {1, 2, 3}
"""

mi_primer_conjunto = {4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 2}

print(mi_primer_conjunto)

"""
Operaciones con conjuntos:

1. Unión: Mezclar dos conjuntos
2. Intersección: Los elementos que tienen en común
3. Diferencia: Los elementos que están en A pero no en B
"""

conjuntoA = {1, 2, 3, 4, 5, 6}
conjuntoB = {2, 4, 6, 8, 10}

print("A Union B:", conjuntoA.union(conjuntoB))
print("A Interseccion B:", conjuntoA.intersection(conjuntoB))
print("A Diferencia B:", conjuntoA.difference(conjuntoB))
print("B Diferencia A:", conjuntoB.difference(conjuntoA))

conjuntoC = set()

conjuntoC.add(True)
conjuntoC.add(2)
conjuntoC.add("Hola Mundo")

print(conjuntoC)

for i in conjuntoC:
  print(i)