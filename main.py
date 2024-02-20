import json
import sqlite3

from flask import Flask, request
app = Flask(__name__)

with open('config.json', 'r') as config_json:
    config = json.load(config_json)

# Nombre de la Base de datos
nombreBD = config["DataBase"]

def conectarBD():
    return sqlite3.connect(nombreBD)

def ejecutarConsulta(consulta):
    connection = conectarBD()
    cursor = connection.cursor()
    
    try:
        print(consulta)
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        connection.commit()
        return resultados
    finally:
        connection.close()


@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

from endpoints import Producto, Furgoneta, Pedido, ProductoEnPedido
