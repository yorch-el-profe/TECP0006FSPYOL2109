import sqlite3
from sqlite3 import Error as SQLiteError

class Cuenta:
  def __init__(self, id, numero_cuenta, saldo, titular):
    self.id = id
    self.numero_cuenta = numero_cuenta
    self.saldo = saldo
    self.titular = titular

def establecer_conexion():
  try:
    conexion = sqlite3.connect('mi_banco.db')
    print("Conectado a SQLite")
    return conexion
  except SQLiteError as e:
    print("Hubo un error al conectar con SQLite")
    print(e)

def crear_tabla(conexion):
  cursor = conexion.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS cuentas (id INT PRIMARY KEY, numero_cuenta VARCHAR(8), saldo REAL, titular VARCHAR(50))")
  print("Tabla creada en la base de datos")

def insertar_informacion(conexion):
  cursor = conexion.cursor()
  cursor.execute("INSERT OR REPLACE INTO cuentas VALUES (1, '12345678', 100, 'Juan Perez')")
  cursor.execute("INSERT OR REPLACE INTO cuentas VALUES (2, '87654321', 200, 'Anahi Salgado')")
  print("Información insertada en la base de datos")

# Incorrecto: Puede sufrir un ataque por SQL Injection
def insertar_cuenta(cuenta):
  cursor = conexion.cursor()
  cursor.executescript("INSERT OR REPLACE INTO cuentas VALUES ({}, '{}', {}, '{}')".format(cuenta.id, cuenta.numero_cuenta, cuenta.saldo, cuenta.titular))

def insertar_cuenta_parametrizado(cuenta):
  parametros = (cuenta.id, cuenta.numero_cuenta, cuenta.saldo, cuenta.titular);

  cursor = conexion.cursor()
  cursor.execute("INSERT OR REPLACE INTO cuentas VALUES (?, ?, ?, ?)", parametros)

conexion = establecer_conexion()

crear_tabla(conexion)
insertar_informacion(conexion)
insertar_cuenta_parametrizado(Cuenta(3, '01020304', 500, 'Liliana Gomez'))

# SQL Injection
insertar_cuenta_parametrizado(Cuenta(4, '88664422', 7500, "'); DELETE FROM cuentas WHERE 1 = 1 OR titular = ('"))

conexion.commit()
conexion.close()