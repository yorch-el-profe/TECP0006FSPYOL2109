import http.client as client

pagina = "www.google.com"
url = "/"

# Estableciendo una conexión por medio de HTTPS a Google
conn = client.HTTPSConnection(pagina)

# Realizar la petición HTTP
conn.request("GET", url)

# Accedo a la respuesta de la petición 
respuesta = conn.getresponse()

# Leer el contenido de la petición (HTML)
data = respuesta.read()

print(data)