"""
Lista:
Colección de elementos de tamaño indefinido y cada elemento tiene su posición.

Sintaxis:
  lista_vacia = list()
  lista_vacia2 = []
  lista = [1,2,3]
"""

numeritos = [10, 20, 30, 40]
#            0    1   2   3

# Acceder a los datos
print(numeritos[2])

# Modificar alguna posición
numeritos[0] = 1000

# Eliminar la posición 1
del numeritos[1]

# Agregar elementos
numeritos.append(400)

print(numeritos)

"""
Agregar elementos utilizando la concatenación
lista = [1,2,3]
lista = [0] + lista -> [0, 1, 2, 3]
lista = lista + [4] -> [0, 1, 2, 3, 4]
"""
numeritos = [True, "Hola Mundo"] + numeritos

print(numeritos)
