"""
Una clase es una plantilla que describe a un objeto. (No se encuentran en memoria)
El objeto puede tener propiedades (atributos de la clase)
y acciones (métodos de la clase)}

Por convención el nombre de las clases utiliza "Pascal Case"

camelCase -> La primera con minúsculas y las siguientes palabras con mayúscula

anitaLavaLaTina

PascalCase -> La primer letra de todas las palabras es mayúscula

AnitaLavaLaTina

snake_case -> Todas las letras minúsculas, palabras separadas por un _

anita_lava_la_tina
"""
class MiPrimerClase:
  pass

"""
Los objetos son "instancias" de una clase.

Una instancia es un espacio en memoria reservado para almacenar y modificar datos.
"""
mi_primer_objeto = MiPrimerClase()

print(mi_primer_objeto)

"""
JavaScript

class Persona {
  nombre = "Juanito";

  saluda() {
    console.log("Hola", this.nombre)
  }
}
"""

# Todos los métodos reciben un parámetro llamado self (= this en JavaScript)
# self es la auto-referencia el objeto
class Persona:
  nombre = "Juanito"
  edad = 17
  pais = "Colombia"

  def saluda(self):
    print("Hola", self.nombre)

juanito = Persona()
otro_juanito = Persona()

print(juanito)

# En Python (y en JS) todo es un objeto
# Notación punto (objeto.propiedad u objeto.metodo())

# Leer el atributo nombre
print(juanito.nombre)

# Modificar un atributo
juanito.edad = 25

print(juanito.edad)

# Agregar nuevas propiedades a un objeto
juanito.ciudad = "Medellin"

print(juanito.ciudad)

# La propiedad ciudad sólo se agrego al objeto "juanito"
# print(otro_juanito.ciudad)

juanito.saluda()