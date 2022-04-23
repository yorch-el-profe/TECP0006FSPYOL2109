from re import search

patron = "lava"
texto = "anita lava la tina"
#        0123456   10

resultado = search(patron, texto)

print(resultado.start(), resultado.end())