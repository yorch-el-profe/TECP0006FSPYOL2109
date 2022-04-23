import requests

url = "https://www.google.com"

respuesta = requests.get(url)

print(respuesta.text)