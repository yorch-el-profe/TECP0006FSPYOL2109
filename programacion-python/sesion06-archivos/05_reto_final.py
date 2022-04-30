import csv
import sqlite3
from sqlite3 import Error as SQLiteError

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
# Leer un archivo CSV
#with open("archivos/inventario.csv", "r", encoding="utf-8") as archivo:
#  reader = csv.reader(archivo)
#  for linea in reader:
#    print(linea)

class Producto:
  def __init__(self, id, producto, precio, cantidad):
    self.id = id
    self.producto = producto
    self.precio = precio
    self.cantidad = cantidad

def establecer_conexion():
  try:
    conexion = sqlite3.connect('mi_inventario.db')
    print("Conectado a SQLite")
    return conexion
  except SQLiteError as e:
    print("Hubo un error al conectar con SQLite")
    print(e)

def crear_tabla(conexion):
  cursor = conexion.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS cuentas (id INT PRIMARY KEY, producto VARCHAR(10), precio REAL, cantidad INT)")
  print("Tabla creada en la base de datos")

def insertar_producto_parametrizado(producto):
  parametros = (producto.id, producto.producto, producto.precio, producto.cantidad);

  cursor = conexion.cursor()
  cursor.execute("INSERT OR REPLACE INTO cuentas VALUES (?, ?, ?, ?)", parametros)

def ver_BD(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM cuentas")
    
    # fetch all the matching rows 
    result = cursor.fetchall()
    # loop through the rows
    for row in result:
        print(row)
        print("\n")

conexion = establecer_conexion()
crear_tabla(conexion)
opcion = 0

while(opcion != "3"):
    print("Menu de opciones:")
    print("1. Ver inventario") # Leer la información de base de datos
    print("2. Agregar un nuevo producto") # Agrega información a la base de datos
    print("3. Salir") # Escribir en el archivo CSV lo que hay en BD
    opcion = input()

    if opcion == "1":
        print("Inventario actual:")
        ver_BD(conexion)
    elif opcion == "2":
        id = input("Ingrese un ID:")
        producto = input("Ingrese el nombre del producto:")
        precio = input("Ingrese un precio:")
        cantidad = input("Ingrese la cantidad de producto:")
        insertar_producto_parametrizado(Producto(id, producto, precio, cantidad))
    elif opcion == "3":
        # Escribir un archivo CSV (w, a)
        with open("archivos/inventario.csv", "w", newline="\n") as archivo:
            writer = csv.writer(archivo)

            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM cuentas")
    
            # fetch all the matching rows 
            result = cursor.fetchall()
            # loop through the rows
            for row in result:
                print(row)
                writer.writerow([row[0], row[1], row[2], row[3]])

conexion.commit()
conexion.close()