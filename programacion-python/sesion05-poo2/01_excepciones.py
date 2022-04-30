"""
Errores (o excepciones) son lanzados en tiempo de ejecución:

* TypeError: Se intenta operar con dos tipos diferentes
* NameError: No existen variables
* ZeroDivisionError: Se intenta dividir entre 0
* ValueError: Se intenta transformar un dato en otro pero no se puede
* RecursionError: Se exceden las autollamadas de una función

Manejo de excepciones (es un manejo genérico, es decir, no me importa el tipo de error):

try:
  bloque que potencialmente puede lanzar un error
except: (atrapa TODOS los errores)
  se ejecutan lineas que controlan el error

Si me interesa captura uno más errores en particular:

try:
  bloque que potencialmente puede lanzar un error (o errores)
except Tipo de Error1:
  bloque que controla el Error1
except Tipo de Error2:
  bloque que controla el Error2
except Exception:
  bloque de error genérico
"""

try:
  print("Ingresa el primer numero:")
  a = int(input())

  print("Ingresa el segundo número:")
  b = int(input())

  print("La suma de " + str(a) + " + " + str(b) + " = " + str(a+b))
except ValueError:
  print("ERROR: Ingresaste un número inválido")
except TypeError:
  print("ERROR: El sistema intento operar datos erroneos")
except Exception:
  print("ERROR: Ocurrió un error inesperado, por favor intente más tarde")