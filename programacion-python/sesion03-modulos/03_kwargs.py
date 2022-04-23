def describir_persona(**datos):
  print(datos)
  print(type(datos))

describir_persona(nombre = "Paquito", edad = 35, domicilio = "Calz de quien sabe donde")

def argumentos(*tupla, **keywords):
  print(tupla, keywords)

argumentos(1,2,3,4,5, algo = "si", nose = "claro")