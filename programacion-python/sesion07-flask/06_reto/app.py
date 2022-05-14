from flask import Flask, render_template, request

app = Flask(__name__)

# Permite que la ruta funcione para peticiones GET y POST
@app.route('/', methods=['GET', 'POST'])
def index():
  mensaje = ""

  if request.method == "POST":
    primer_numero = int(request.form["primer_numero"])
    segundo_numero = int(request.form["segundo_numero"])
    operacion = int(request.form["operacion"])

    resultado = 0
    simbolo = ""

    if operacion == 1:
      resultado = primer_numero + segundo_numero
      simbolo = "+"
    elif operacion == 2:
      resultado = primer_numero - segundo_numero
      simbolo = "-"
    elif operacion == 3:
      resultado = primer_numero * segundo_numero
      simbolo = "*"
    else:
      resultado = "ERROR"

    mensaje = "{} {} {} = {}".format(primer_numero, simbolo, segundo_numero, resultado)
  
  return render_template('index.html', mensaje = mensaje)
