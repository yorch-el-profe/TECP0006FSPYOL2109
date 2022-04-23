class Persona:
  def __init__(self, nombre = "Joaquin", edad = 50, pais = "México"):
    self.nombre = nombre
    self.edad = edad
    self.pais = pais
  
  def saluda(self):
    print("Hola", self.nombre)

  # Ayuda a mostrar al objeto de una mejor manera
  # al momento del print
  def __str__(self):
    return "Nombre: {}, Edad: {}, Pais: {}".format(self.nombre, self.edad, self.pais)

  def __eq__(self, otro):
    return self.nombre == otro.nombre and self.edad == otro.edad and self.pais == otro.pais

joaquin = Persona()
ramiro = Persona("Ramiro", 40, "Perú")
joaquin2 = Persona()

print(joaquin)
print(ramiro)
print(joaquin == joaquin2)
print(joaquin is joaquin2)

