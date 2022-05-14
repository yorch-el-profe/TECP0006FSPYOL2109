from flask import Flask, render_template, request

app = Flask(__name__)

# Permite que la ruta funcione para peticiones GET y POST
@app.route('/', methods=['GET', 'POST'])
def index():
  mensaje = ""

  if request.method == "POST":
    primer_numero = int(request.form["primer_numero"])
    segundo_numero = int(request.form["segundo_numero"])

    resultado = primer_numero + segundo_numero

    mensaje = "{} + {} = {}".format(primer_numero, segundo_numero, resultado)
  
  return render_template('index.html', mensaje = mensaje)
