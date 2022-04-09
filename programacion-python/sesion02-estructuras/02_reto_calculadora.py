print("Dame el primer número:")
numero1 = float(input())

print("Dame el segundo número:")
numero2 = float(input())

print("[CALCULADORA]")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Implementar el código para preguntar al usuario que operación realizar
# y mostrar el resultado

# RESPUESTA:

opcion = int(input())
if opcion ==  1:
    print("Suma:  {} + {} = {}".format(numero1, numero2, numero1 + numero2))
elif opcion == 2:
    print("Resta:  {} - {} = {}".format(numero1, numero2, numero1 - numero2))
elif opcion == 3:
    print("Multiplicación:  {} * {} = {}".format(numero1, numero2, numero1 * numero2))
elif opcion == 4:
    print("División:  {} / {} = {}".format(numero1, numero2, numero1 / numero2))
else:
    print("ingrese una opcion valida")