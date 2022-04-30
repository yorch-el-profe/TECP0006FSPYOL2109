import csv

# Leer un archivo CSV
with open("archivos/padron_electoral_fake.csv", "r", encoding="utf-8") as archivo:
  reader = csv.reader(archivo)
  for linea in reader:
    print(linea)

# Escribir un archivo CSV (w, a)
with open("archivos/padron_electoral_fake.csv", "a", newline="\n") as archivo:
  writer = csv.writer(archivo)
  writer.writerow(["Paquito Perez", 18, "Calz Ermita, Iztapalapa"])