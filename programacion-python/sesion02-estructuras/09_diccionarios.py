"""
Diccionario

Es una colección de llaves-valores, las llaves son cadenas de texto y los valores
pueden ser lo que sea.

Sintaxis:
{
  "nombre": "Jorge",
  "edad": 30,
  "vacunado": True
}
"""

carro = {
  "marca": "Volkswagen",
  "modelo": "Beetle",
  "placas": "ABC-123",
  "año": 2021,
  "pagoTenencia": False
}

# Acceder a una llave
print(carro["marca"])

# Agregar nuevas llaves
carro["fechaCompra"] = "10/01/2022"

# Eliminar una llave/valor
del carro["placas"]

print(carro)
print(carro.keys())
print(carro.values())
print(carro.items())

for key, value in carro.items():
  print(key, value)