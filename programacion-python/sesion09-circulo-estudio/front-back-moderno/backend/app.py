from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)

"""
  CORS: Cross-Origin Resource Script
  Es un problema cuando un dominio A intenta acceder a un dominio B.

  Con la siguiente línea, habilitamos que cualquier dominio (o puerto)
  acceda a nuestra aplicación de flask
"""
cors = CORS(app)

@app.route('/razas')
def razas():
  response = requests.get('https://dog.ceo/api/breeds/list/all')
  json = response.json()
  return jsonify({ "data": list(json["message"].keys()) })

@app.route('/razas/<nombre>')
def imagen_raza(nombre):
  response = requests.get('https://dog.ceo/api/breed/{}/images/random'.format(nombre))
  json = response.json()
  return jsonify({ "data": json["message"] })