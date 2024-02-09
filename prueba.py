from flask import Flask, request
import sqlite3

# Nombre de la Base de datos
nombreBD = "HomeX.db"

app = Flask(__name__)

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

# Devuelve una lista de Pedidos
@app.route('/Pedidos', methods=['GET'])
def GetListaPedidos():
    connection = sqlite3.connect(nombreBD)
    cursor = connection.cursor()
    resultado = cursor.execute('SELECT * FROM Pedido').fetchall()
    connection.close()
    return resultado

# Devuelve una lista de Pedidos en cierta fecha
@app.route('/Pedidos/<string:fecha>', methods=['GET'])
def GetListaPedidosEnFecha(fecha):
    connection = sqlite3.connect(nombreBD)
    cursor = connection.cursor()
    resultado = cursor.execute(f'SELECT * FROM Pedido WHERE Pedido.date = \'{fecha}\'').fetchall()
    connection.close()
    return resultado

@app.route('/Pedido/<int:idPedido>', methods=['GET'])
def GetPedidoById(idPedido):
    connection = sqlite3.connect(nombreBD)
    cursor = connection.cursor()
    resultado = cursor.execute(f'SELECT * FROM Pedido WHERE Pedido.id = \'{idPedido}\'').fetchall()
    connection.close()
    return resultado

@app.route('/CrearPedido', methods=['POST'])
def PostPedido():
    respuesta = ''
    try:
        connection = sqlite3.connect(nombreBD)
        cursor = connection.cursor()

        date = request.form['date']
        address = request.form['address']
        idFurgoneta = request.form['idFurgoneta']

        cursor.execute(f'INSERT INTO Pedido (date, address, idFUrgoneta) VALUES (\'{date}\', \'{address}\', \'{idFurgoneta}\')')

        connection.commit()
        connection.close()
        respuesta = 'Pedido creado correctamente'
    except Exception as error:
        respuesta = f'Error al crear el pedido: {str(error)}'
    finally:
        return respuesta
