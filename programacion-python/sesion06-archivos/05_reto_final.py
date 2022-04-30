"""
Objetivo:

Leer el archivo inventario.csv e insertarlo en una base de datos SQLite.

Adicional, crear un menú interactivo (línea de comandos) en el cuál
el usuario pueda ver el inventario actual y pueda agregar un nuevo
producto.

Al finalzar la ejecución del programa, actualizar el CSV con lo que hay
en la base de datos.
"""

# Al iniciar el programa hay que leer el CSV para insertarlo en BD

print("Menu de opciones:")
print("1. Ver inventario") # Leer la información de base de datos
print("2. Agregar un nuevo producto") # Agrega información a la base de datos
print("3. Salir") # Escribir en el archivo CSV lo que hay en BD