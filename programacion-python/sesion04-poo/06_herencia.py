from urllib.request import ProxyDigestAuthHandler


class Animal:
  nombre = ""
  edad = 0

  def morir(self):
    print("x.x")

class Perro(Animal):
  raza = ""
  color = ""
  vacunas = []

  def ladrar(self):
    print("wooff!!")

perro = Perro()
perro.ladrar()
perro.morir()

class Producto:
  def __init__(self, nombre, precio, etiquetas, ingredientes):
    self.nombre = nombre
    self.precio = precio
    self.etiquetas = etiquetas
    self.ingredientes = ingredientes

  def cualquier_metodo(self):
    print("Soy cualquier metodo de Producto")

  def __str__(self):
    return "{} - ${}".format(self.nombre, self.precio)

class Refresco(Producto):
  def __init__(self, nombre, precio, etiquetas, ingredientes, sabor):
    super().__init__(nombre,precio, etiquetas, ingredientes)
    self.sabor = sabor

  def __str__(self):
    return super().__str__() + " - {}".format(self.sabor)

pepsi = Refresco("Pepsi 600ml", 12, ["azucares", "calorias"], [], "cola")
print(pepsi)