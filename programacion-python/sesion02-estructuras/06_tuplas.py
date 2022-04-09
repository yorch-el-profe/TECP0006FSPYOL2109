"""
Tuplas

Permite almacenar valores CONSTANTES (textos, numeros, booleanos, etc) y
TIENEN UN TAMAÑO FIJOOOOOOOOOOOOO!!!!!!!!

Sintaxis:
variable = (elem1, elem2, elem3, ..., elemenN)

Para crear una tupla con 1 sólo elemento debe agregarse una ,
al final, es decir:

(5,)
"""

mi_primer_tupla = (1,2,3,4,5)

print(mi_primer_tupla)
print(type(mi_primer_tupla))

tupla_un_elemento = (1,)

print(tupla_un_elemento)
print(type(tupla_un_elemento))

# Para acceder a los elementos se necesita conocer su posición

tupla_mixta = (1, "hola", True, 100, 1 + 2j)
#              0    1      2     3     4

# Para acceder al elemento en la posición 2
# [n] -> Accedemos a la posición n
print(tupla_mixta[2])

# Concatenar tuplas

tuplaA = (1,2,3)
tuplaB = (4,5,6)
tuplaC = tuplaA + tuplaB

print(tuplaC)
print(len(tuplaC)) # len() obtiene el tamaño de una tupla