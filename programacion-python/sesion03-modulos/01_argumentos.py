"""
Solución básica (se usa un sólo parámetro como un arreglo)
def sum_all(list):
  total = 0
  for i in list:
    total += i # total = total + i
  return total

numeritos = []

while True:
  print("Elige alguna opción:")
  print("1. Ingresa un número a sumar")
  print("2. Sumar todos los números")
  opcion = int(input())

  if opcion == 1:
    print("Ingresa un número:")
    numero = int(input())
    numeritos.append(numero)
  elif opcion == 2:
    resultado = sum_all(numeritos)
    print("La suma de todos los números es: {}".format(resultado))
    break
  else:
    print("Opción inválida")
"""

# En python, los parámetros con * al principio significa
# que se recibe una cantidad INDETERMINADA de los mismos
def sum_all(*numeros):
  print(numeros)
  total = 0
  for i in numeros:
    total += i
  return total

numeritos = []

while True:
  print("Elige alguna opción:")
  print("1. Ingresa un número a sumar")
  print("2. Sumar todos los números")
  opcion = int(input())

  if opcion == 1:
    print("Ingresa un número:")
    numero = int(input())
    numeritos.append(numero)
  elif opcion == 2:
    resultado = sum_all(*numeritos) # es como hacer sum_all(numeritos[0], numeritos[1], ...)
    print("La suma de todos los números es: {}".format(resultado))
    break
  else:
    print("Opción inválida")