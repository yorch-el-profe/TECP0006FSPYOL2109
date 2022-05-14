from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', mensaje = "Hola desde Python con Flask!!!")