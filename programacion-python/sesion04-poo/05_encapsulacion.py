class CuentaBancaria:

  def __init__(self, saldo = 0):
    self.__saldo = saldo

  def abonar(self, saldo):
    if saldo <= 0:
      print("Error")
    
    self.__saldo += saldo

  def retirar(self, monto):
    if monto > self.__saldo:
      print("Error")
    
    self.__saldo -= monto

  def estado_cuenta(self):
    return self.__saldo

cuenta = CuentaBancaria(100)

cuenta.abonar(500)
cuenta.retirar(300)

# Nueva propiedad
cuenta.__saldo = 100000000000

print(cuenta.estado_cuenta())
print(cuenta.__saldo)