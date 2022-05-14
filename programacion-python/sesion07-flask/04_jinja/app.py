from flask import Flask, render_template

app = Flask(__name__)

productos = [
  { "id": 1, "nombre": "Gelatina Gary Sabor Frambuesa", "precio": 10 },
  { "id": 2, "nombre": "Paleta Payaso", "precio": 12 },
  { "id": 3, "nombre": "Cheetos Torciditos", "precio": 10 }
]

@app.route('/')
def index():
  return render_template('index.html', productos = productos )