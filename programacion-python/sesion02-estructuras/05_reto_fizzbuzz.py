"""
Problema: 

Dados los números del 1 al 100:
  * Si el número es divisible entre 3, imprimir en pantalla Fizz
  * Si el número es divisible entre 5, imprimir en pantalla Buzz
  * Si el número es divisible entre 3 y 5, imprimir en pantalla FizzBuzz

Posible salida:
1
2
Fizz (3)
4
Buzz (5)
Fizz (6)
7
8
Fizz (9)
Buzz (10)
11
Fizz (12)
13
14
FizzBuzz (15)
"""
mensaje = ""

for i in range(1, 101):
  if (i%3==0):
    mensaje = "Fizz"
      
  if (i%5==0):
    mensaje = mensaje + "Buzz "

  mensaje = mensaje + " ({})".format(i)
  print(mensaje)
  mensaje = ""