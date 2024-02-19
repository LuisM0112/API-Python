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
        cursor.execute(consulta)
        print(consulta)

        resultados = cursor.fetchall()
        connection.commit()
        return resultados
    finally:
        connection.close()


@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

# Devuelve una lista de Furgonetas
@app.route('/Furgonetas', methods=['GET'])
def GetListaFurgonetas():
    connection = sqlite3.connect(nombreBD)
    cursor = connection.cursor()
    resultado = cursor.execute('SELECT * FROM Furgoneta').fetchall()
    connection.close()
    return resultado

@app.route('/Furgoneta/<string:matricula>', methods=['GET'])
def GetFurgonetaByMatricula(matricula):
    connection = sqlite3.connect(nombreBD)
    cursor = connection.cursor()
    resultado = cursor.execute(f'SELECT * FROM Furgoneta WHERE Furgoneta.matricula = \'{matricula}\'').fetchall()
    connection.close()
    return resultado

from endpoints import Furgoneta, Pedido, ProductoEnPedido
