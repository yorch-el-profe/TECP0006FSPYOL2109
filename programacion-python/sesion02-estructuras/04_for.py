"""
  For itera una estructura

  Sintaxis:
    for variable in estructura:
      lineas de codigo
"""

print(range(0, 10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Imprimir los primeros 20 números naturales

"""
  i = 1

  while i <= 20:
    print(i)
    i = i + 1
"""
#for numero in range(1, 21):
#  print(numero)

# La suma de los primeros N números
print("Dame la cantidad de números:")
n = int(input())

suma = 0

for i in range(1, n + 1):
  suma = suma + i

print("La suma de los primeros {} números es {}".format(n, suma))