def saluda(*nombres, idioma = "es"):
  saludo = "Hola"

  if idioma == "en":
    saludo = "Hi"
  elif idioma == "fr":
    saludo = "Bonjour"
  elif idioma == "de":
    saludo = "Hallo"
  
  for nombre in nombres:
    print(saludo, nombre, sep = ", ")

saluda("Alberto", "Daniel", "Abelardo", "Juan", "Leonardo", "Daniela", "Josefina", idioma = "en")

