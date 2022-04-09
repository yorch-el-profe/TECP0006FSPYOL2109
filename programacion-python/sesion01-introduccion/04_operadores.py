# Operadores numéricos

# Suma (+)
print(1 + 2)

# Resta (-)
print(5 - 6)

# Multiplicación (*)
print(7 * 8)

# División (/)
print(6 / 3)

# División entera (//)
print(5 / 2) # 2.5
print(5 // 2) # 2

# Residuo / Módulo (%)
print(5 % 2) # 1

# Concatenación (unión de dos (o más) cadenas de texto)
nombre_completo = "Jorge" + " " + "Ramón"
print(nombre_completo)

# La concatenación es únicamente entre cadenas de texto
suma = 1 + 3
# print("La suma de 1 + 3 es: " + suma) ❌

# La manera correcta es convertir a una cadena de texto
# se usa la función str()
print("La suma de 1 + 3 es: " + str(suma)) # ✔

nombre = "Paquito"
apellido = "Sanchez"
edad = 34

# print("Hola, mi nombre es " + nombre + " " + apellido + " y tengo " + str(edad) + " años") ❌

# Formato (format)
print("Hola, mi nombre es {} {} y tengo {} años".format(nombre, apellido, str(edad)))

# Operadores lógicos

"""
  Otros lenguajes
    && y lógico (el valor es verdadero si ambos son verdaderos)
    || o lógico (el valor es verdadero si alguno es verdadero)
    !  negación

  Python
    and
    or
    not
"""
operacion_and = True and True # True
operacion_or = False or not False # True

# Comparaciones (>, <, >=, <=, ==, !=)

num1 = 10
num2 = 20

print(num1 > num2)
print(num1 <= num2)
print(num1 == num2)
print(num1 != num2)