"""
  Para transformar un STRING a NÚMERO se utilizan las funciones:
    int() -> números enteros
    float() -> números flotantes

  Recordando que str() -> string
"""

print("Dame el primer número:")
numero1 = float(input()) # Transformando la salida directamente en un float

print("Dame el segundo número:")
numero2 = float(input())

resultado = numero1 + numero2

print("{} + {} = {}".format(numero1, numero2, resultado))