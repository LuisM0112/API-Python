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

@app.route('/Pedido', methods=['POST'])
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

@app.route('/Pedido/<int:idPedido>', methods=['PUT'])
def PutPedido(idPedido):
    respuesta = ''
    try:
        connection = sqlite3.connect(nombreBD)
        cursor = connection.cursor()

        newDate = request.form.get('date')
        newAddress = request.form.get('address')
        newIdFurgoneta = request.form.get('idFurgoneta')

        cursor.execute(f"SELECT date, address, idFurgoneta FROM Pedido WHERE id = \'{idPedido}\'")
        currentValues = cursor.fetchone()
        if currentValues:
            currentDate, currentAddress, currentIdFurgoneta = currentValues
        else:
            raise ValueError("Pedido no encontrado")

        if newDate:
            currentDate = newDate
        if newAddress:
            currentAddress = newAddress
        if newIdFurgoneta:
            currentIdFurgoneta = newIdFurgoneta

        cursor.execute(f"UPDATE Pedido SET date = \'{currentDate}\', address = \'{currentAddress}\', idFurgoneta = \'{currentIdFurgoneta}\' WHERE id = \'{idPedido}\'")

        connection.commit()
        connection.close()
        respuesta = 'Pedido modificado correctamente'
    except Exception as error:
        respuesta = f'Error al modificar el pedido: {str(error)}'
    finally:
        return respuesta

@app.route('/ProductoEnPedido/<int:idPedido>', methods=['POST'])
def PostProductoEnPedido(idPedido):
    respuesta = ''
    try:
        connection = sqlite3.connect(nombreBD)
        cursor = connection.cursor()

        idProducto = request.form.get('idProducto')
        cantidad = request.form.get('Cantidad')

        cursor.execute(f"SELECT * FROM Pedido WHERE id = \'{idPedido}\'")
        pedido = cursor.fetchone()
        if not pedido:
            raise ValueError("Pedido no encontrado")
        elif not idProducto:
            raise ValueError("Producto no encontrado")
        elif not cantidad or cantidad < 1:
            raise ValueError("Cantidad no válida")
        else:
            cursor.execute(f"INSERT INTO ProductoEnPedido (idPedido, idProducto, cantidad) VALUES (\'{idPedido}\', \'{idProducto}\', \'{cantidad}\'")

        connection.commit()
        connection.close()
        respuesta = 'Producto añadido al pedido correctamente'
    except Exception as error:
        respuesta = f'Error al añadir producto al pedido: {str(error)}'
    finally:
        return respuesta

@app.route('/ProductoEnPedido/<int:idPedido>', methods=['DELETE'])
def DeleteProductoEnPedido(idPedido):
    respuesta = ''
    try:
        connection = sqlite3.connect(nombreBD)
        cursor = connection.cursor()
        idProducto = request.form.get('idProducto')

        cursor.execute(f"SELECT * FROM Pedido WHERE id = \'{idPedido}\'")
        pedido = cursor.fetchone()
        if not pedido:
            raise ValueError("Pedido no encontrado")
        elif not idProducto:
            raise ValueError("Producto no encontrado")
        else:
            cursor.execute(f"DELETE FROM ProductoEnPedido WHERE idPedido = \'{idPedido}\' AND idProducto = \'{idProducto}\'")

        connection.commit()
        connection.close()
        respuesta = 'Producto eliminado correctamente del pedido'
    except Exception as error:
        respuesta = f'Error al eliminar el procuto del pedido: {str(error)}'
    finally:
        return respuesta

@app.route('/ProductoEnPedido/<int:idPedido>', methods=['PUT'])
def PutProductoEnPedido(idPedido):
    respuesta = ''
    try:
        connection = sqlite3.connect(nombreBD)
        cursor = connection.cursor()
        idProducto = request.form.get('idProducto')
        cantidad = request.form.get('Cantidad')

        cursor.execute(f"SELECT * FROM Pedido WHERE id = \'{idPedido}\'")
        pedido = cursor.fetchone()
        if not pedido:
            raise ValueError("Pedido no encontrado")
        elif not idProducto:
            raise ValueError("Producto no encontrado")
        else:
            cursor.execute(f"UPDATE ProductoEnPedido SET cantidad = \'{cantidad}\' WHERE idPedido = \'{idPedido}\' AND idProducto = \'{idProducto}\'")

        connection.commit()
        connection.close()
        respuesta = 'Producto del pedido modificado correctamente'
    except Exception as error:
        respuesta = f'Error al modificar el procuto del pedido: {str(error)}'
    finally:
        return respuesta

@app.route('/Pedido/<int:idPedido>', methods=['DELETE'])
def DeletePedido(idPedido):
    respuesta = ''
    try:
        connection = sqlite3.connect(nombreBD)
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM Pedido WHERE id = \'{idPedido}\'")
        pedido = cursor.fetchone()
        if not pedido:
            raise ValueError("Pedido no encontrado")
        else:
            cursor.execute(f"DELETE FROM ProductoEnPedido WHERE idPedido = \'{idPedido}\'")
            cursor.execute(f"DELETE FROM Pedido WHERE id = \'{idPedido}\'")

        connection.commit()
        connection.close()
        respuesta = 'Pedido eliminado correctamente'
    except Exception as error:
        respuesta = f'Error al eliminar el pedido: {str(error)}'
    finally:
        return respuesta


@app.route('/Furgoneta', methods=['POST'])
def PostFurgoneta():
    respuesta = ''
    try:
        connection = sqlite3.connect(nombreBD)
        cursor = connection.cursor()

        matricula = request.form['matricula']
        marca = request.form['marca']
        modelo = request.form['modelo']
        idFurgoneta = request.form['idFurgoneta'] 

        cursor.execute(f'INSERT INTO Furgoneta (matricula, marca, modelo, idFurgoneta) VALUES (\'{matricula}\', \'{marca}\', \'{modelo}\', \'{idFurgoneta}\')')

        connection.commit()
        connection.close()
        respuesta = 'Furgoneta creada correctamente'
    except Exception as error:
        respuesta = f'Error al crear la furgoneta: {str(error)}'
    finally:
        return respuesta

@app.route('/Furgoneta/<int:idFurgoneta>', methods=['PUT'])
def PutFurgoneta(idFurgoneta):
    respuesta = ''
    try:
        connection = sqlite3.connect(nombreBD)
        cursor = connection.cursor()

        nueva_marca = request.form.get('marca')
        nuevo_modelo = request.form.get('modelo')
        nueva_idFurgoneta = request.form.get('idFurgoneta')

        cursor.execute(f"SELECT marca, modelo, idFurgoneta FROM Furgoneta WHERE idFurgoneta = \'{idFurgoneta}\'")
        valores_actuales = cursor.fetchone()
        if valores_actuales:
            marca_actual, modelo_actual, idFurgoneta_actual = valores_actuales
        else:
            raise ValueError("Furgoneta no encontrada")

        if nueva_marca:
            marca_actual = nueva_marca
        if nuevo_modelo:
            modelo_actual = nuevo_modelo
        if nueva_idFurgoneta:
            idFurgoneta_actual = nueva_idFurgoneta

        cursor.execute(f"UPDATE Furgoneta SET marca = \'{marca_actual}\', modelo = \'{modelo_actual}\', idFurgoneta = \'{idFurgoneta_actual}\' WHERE idFurgoneta = \'{idFurgoneta}\'")

        connection.commit()
        connection.close()
        respuesta = 'Furgoneta modificada correctamente'
    except Exception as error:
        respuesta = f'Error al modificar la furgoneta: {str(error)}'
    finally:
        return respuesta

@app.route('/Furgoneta/<int:idFurgoneta>', methods=['DELETE'])
def DeleteFurgoneta(idFurgoneta):
    respuesta = ''
    try:
        connection = sqlite3.connect(nombreBD)
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM Furgoneta WHERE idFurgoneta = \'{idFurgoneta}\'")
        furgoneta = cursor.fetchone()
        if not furgoneta:
            raise ValueError("Furgoneta no encontrada")
        else:
            cursor.execute(f"DELETE FROM Furgoneta WHERE idFurgoneta = \'{idFurgoneta}\'")

        connection.commit()
        connection.close()
        respuesta = 'Furgoneta eliminada correctamente'
    except Exception as error:
        respuesta = f'Error al eliminar la furgoneta: {str(error)}'
    finally:
        return respuesta
