"""
Las funciones en Python son de orden superior.

Son funciones que reciben funciones y regresan funciones.

def funcion_a():
  print("Ejecutando A")

def funcion_b(f):
  print("Ejecutando B")
  f()

funcion_b(funcion_a)

def funcion_c():
  def funcion_d():
    print("Ejecutando D")
  
  return funcion_d

f = funcion_c()
f()
"""

"""
Un decorador es una función que se ejecuta PRIMERO que otra función.

Para crear un decorador se necesita crear una función que regrese otra función
y sustituirá a la original.
"""

""" PRIMER EJEMPLO DE DECORADOR
def mi_primer_decorador(funcion_original):
  print("Ejecutando mi primer decorador")

  def sustituto():
    print("Función sustito")
    funcion_original()

  return sustituto

@mi_primer_decorador
def hello_world():
  print("Hello World")

hello_world()
"""

def validar_numeros(suma_numerica):
  def suma_numerica_sustito(a, b):
    try:
      return suma_numerica(int(a), int(b))
    except:
      return 0

  return suma_numerica_sustito


@validar_numeros
def suma_numerica(a, b):
  return a + b

print(suma_numerica(10, "200a"))