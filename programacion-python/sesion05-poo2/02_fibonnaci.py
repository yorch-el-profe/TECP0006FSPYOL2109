from fibonacci import *
from fibonacci_error import FibonacciError

try:
  print("Ingresa el número que quieres conocer de la secuencia de fibonacci:")
  entrada = int(input())
  resultado = fibonacci(entrada)
  print(resultado)
except ValueError:
  print("ERROR: Ingresaste un número inválido")
except FibonacciError:
  print("ERROR: Fibonacci no puede operar con números negativos")
except RecursionError:
  print("ERROR: Se intentó calcular un número muy grande para el algoritmo")
except Exception:
  print("ERROR: Ocurrió un error inesperado, intente más tarde")