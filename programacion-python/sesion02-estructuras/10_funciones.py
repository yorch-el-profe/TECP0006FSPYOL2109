# DRY (Don't Repeat Yourself)

"""
Función
Un bloque de código que recibe parámetros y regresa una salida (opcionalmente).

Sintaxis:
def nombre_de_la_funcion(param1, param2, param3):
  bloque de codigo
"""
def mi_primer_funcion():
  print("Hola Mundo desde una función")

mi_primer_funcion()

def saluda(nombre):
  print("Hola,", nombre)

saluda("Elver Galarga")

def suma(a, b):
  return a + b

print("La suma 1 + 3 es:", suma(1, 3))

# Definir valor por default para los parámetros
# Los parámetros opcionales van al final de la definición
def sumaMejorada(a = 0, b = 0):
  return a + b

print(sumaMejorada(100))

"""
High Order Functions

* Funciones que reciben funciones como parámetro
* Funciones que regresan funciones
"""
def imprimir(algo):
  print(algo)

def saluda2(log, nombre):
  log("Hola," + nombre)

saluda2(imprimir, "Paquito")

def funcion1():
  print("Ejecutando funcion1")

  def funcion2():
    print("Ejecutando funcion2")

  return funcion2

f = funcion1()
f()

# Función que sume los primeros N números
def sum_all(n):
  total = 0
  for i in range(0, n + 1):
    total = total + i
  return total

print(sum_all(10))