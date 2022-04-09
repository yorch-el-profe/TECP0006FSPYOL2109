# While: Se repite el bloque de código hasta dejar de cumplir la condición
#i = 1

#while i <= 10:
#  print(i)
#  i = i + 1

print("Dame el primer número:")
numero1 = float(input())

print("Dame el segundo número:")
numero2 = float(input())

while True:
  print("\n[CALCULADORA]")
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. Dividir")
  print("5. Salir")

  opcion = int(input())

  if opcion ==  1:
      print("Suma:  {} + {} = {}".format(numero1, numero2, numero1 + numero2))
  elif opcion == 2:
      print("Resta:  {} - {} = {}".format(numero1, numero2, numero1 - numero2))
  elif opcion == 3:
      print("Multiplicación:  {} * {} = {}".format(numero1, numero2, numero1 * numero2))
  elif opcion == 4:
      print("División:  {} / {} = {}".format(numero1, numero2, numero1 / numero2))
  elif opcion == 5:
    break
  
  if opcion < 1 or opcion > 5:
    print("Ingrese una opción válida")