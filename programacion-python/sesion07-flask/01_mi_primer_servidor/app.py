from flask import Flask

# Iniciar la aplicación
app = Flask(__name__)

# Definiendo una ruta principal (raíz)
@app.route('/')
def hello_world():
  return "hello world"

@app.route('/greeting')
def greeting():
  return "Hola como estas"

# Esta línea se agrega si se ejecuta el archivo
# directamente con el comando python
# app.run()