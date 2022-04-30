import sqlite3
from sqlite3 import Error as SQLiteError

try:
  conexion = sqlite3.connect('mi_base_datos.db')
  print("Conectado a SQLite")
except SQLiteError as e:
  print("Hubo un error al conectar con SQLite")
  print(e)
finally: # Se ejecuta independientemente si hubo un error o no
  conexion.close()