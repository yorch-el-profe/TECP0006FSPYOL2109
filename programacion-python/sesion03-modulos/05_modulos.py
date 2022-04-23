#Importar funciones/clases/variables de un archivo

# 1. Importar todo el modulo
# import modulo as otro_nombre

import calculadora as calc

print("La suma de 1 + 2 = {}".format(calc.suma(1,2)))

# 2. Importar algo muy específico
# from modulo import cosa1, cosa2, cosa3, ..., cosa4

from calculadora import resta

print("La resta de 10 - 2 = {}".format(resta(10, 2)))

# 3. Importar todo sin utilizar el nombre del módulo
# from modulo import *

from calculadora import *

print("La multiplicación de 200 * 40 = {}".format(multiplicacion(200,40)))

print(raiz_cuadrada(4))