"""
class Persona:
  nombre = "Juanito"
  edad = 17
  pais = "Colombia"

  def saluda(self):
    print("Hola", self.nombre)

juanito = Persona()
ricardo = Persona()

ricardo.nombre = "Ricardo"
ricardo.edad = 20
ricardo.pais = "Argentina"
"""

"""
En POO un constructor es una función "especial" que se ejecuta
al instanciar un objeto.
"""

class Persona:
  def __init__(self, nombre = "Joaquin", edad = 50, pais = "México"):
    self.nombre = nombre
    self.edad = edad
    self.pais = pais
  
  def saluda(self):
    print("Hola", self.nombre)

ricardo = Persona("Ricardo", 22, "Argentina")
joaquin = Persona()

ricardo.saluda()
joaquin.saluda()