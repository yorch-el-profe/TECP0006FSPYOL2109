"""
  Estructuras de decisión (if)

  if condicion:
    instruccion1
    instruccion2
    .
    .
  elif condicion:
    .
    .
    .
  else:
    .
    .
    .
"""
print("Dame tu edad:")
edad = int(input())

if edad < 18 and edad >= 0:
  print("Eres menor de edad")
elif edad < 0:
  print("Apoco tienes años negativos?!")
else:
  print("Eres mayor de edad")