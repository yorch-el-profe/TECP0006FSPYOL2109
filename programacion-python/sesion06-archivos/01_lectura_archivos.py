"""
open("ubicación del archivo", "modo")
"""
# Leer las líneas de un archivo (r)
with open("archivos/test.txt", "r") as archivo:
  for linea in archivo:
    print(linea)

# Escribir en un archivo (w)
with open("archivos/test.txt", "w") as archivo:
  archivo.write("Hola Mundo desde Python")
  archivo.writelines(["\nLinea 1", "\nLinea 2", "\nLinea 3", "\nLinea 4"])

# Agregar nuevas lineas (a)
with open("archivos/test.txt", "a") as archivo:
  archivo.write("\nAgregando una nueva línea que técnicamente no debería borrar lo anterior")