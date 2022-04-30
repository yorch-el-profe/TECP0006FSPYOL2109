"""
Maquina Expendedora

1. Es una máquina de refrescos, por lo tanto la máquina por dentro tiene N refrescos
2. Estos refrescos tienen una marca y un precio
3. Para comprar un refresco, se necesita la marca del producto y el dinero
4. Al momento de comprar el refresco, se debe "descontar" el refresco del inventario de la máquina
5. Esta máquina no debe ser manipulable por alguien externo

maquina = MaquinaExpendedora()

maquina.comprar("Pepsi", 100) -> 85 (y quita el refresco de la máquina)
maquina.revisar() -> Lista de los refrescos que hay
"""
class Refresco:
  def __init__(self, nombre, precio):
    self.nombre = nombre
    self.precio = precio

  def __str__(self):
    return "{} - ${}".format(self.nombre, self.precio)

  def __eq__(self, refresco):
    return self.nombre == refresco.nombre


class MaquinaExpendedora:

  def __init__(self):
    self.__refrescos = [
      Refresco("Coca Cola 600ml", 15),
      Refresco("Topochico 500ml", 14),
      Refresco("Pepsi 400ml", 13),
      Refresco("Coca Cola 600ml", 15),
      Refresco("Coca Cola 250ml", 10)
    ]

  def ver_refrescos(self):
    print("Lista de refrescos:")
    for refresco in self.__refrescos:
      print(refresco)

  def comprar(self, nombre):
    for i in range(0, len(self.__refrescos)):
      if nombre == self.__refrescos[i].nombre:
        return self.__refrescos.pop(i)
    
    return "No encontrado"

maquina = MaquinaExpendedora()
maquina.ver_refrescos()

print("\n")

compra = maquina.comprar("Coca Cola 600ml")
print(compra)

compra = maquina.comprar("Pepsi 400ml")
print(compra)

compra = maquina.comprar("Fanta 1lt")
print(compra)

print("\n")

maquina.ver_refrescos()