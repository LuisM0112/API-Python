from flask import request
from prueba import app, ejecutarConsulta

@app.route('/Pedidos', methods=['GET'])
def GetListaPedidos():
  respuesta = ''
  try:
    consulta = 'SELECT * FROM Pedido'
    respuesta = ejecutarConsulta(consulta)
  except Exception as error:
    respuesta = f'Error al obtener la lista de pedidos: {str(error)}'
  finally:
    return respuesta

# Devuelve una lista de Pedidos en cierta fecha
@app.route('/Pedidos/<string:fecha>', methods=['GET'])
def GetListaPedidosEnFecha(fecha):
  respuesta = ''
  try:
    consulta = f'SELECT * FROM Pedido WHERE Pedido.date = \'{fecha}\''
    respuesta = ejecutarConsulta(consulta)
  except Exception as error:
    respuesta = f'Error al obtener la lista de pedidos: {str(error)}'
  finally:
    return respuesta

@app.route('/Pedido/<int:idPedido>', methods=['GET'])
def GetPedidoById(idPedido):
  respuesta = ''
  try:
    consulta = f'SELECT * FROM Pedido WHERE Pedido.id = \'{idPedido}\''
    respuesta = ejecutarConsulta(consulta)
  except Exception as error:
    respuesta = f'Error al obtener la lista de pedidos: {str(error)}'
  finally:
    return respuesta

@app.route('/Pedido', methods=['POST'])
def PostPedido():
  respuesta = ''
  try:
    date = request.form['date']
    address = request.form['address']
    idFurgoneta = request.form['idFurgoneta']

    consulta = f'INSERT INTO Pedido (date, address, idFUrgoneta) VALUES (\'{date}\', \'{address}\', \'{idFurgoneta}\')'
    ejecutarConsulta(consulta)

    respuesta = 'Pedido creado correctamente'
  except Exception as error:
    respuesta = f'Error al crear el pedido: {str(error)}'
  finally:
    return respuesta

@app.route('/Pedido/<int:idPedido>', methods=['PUT'])
def PutPedido(idPedido):
  respuesta = ''
  try:
    newDate = request.form.get('date')
    newAddress = request.form.get('address')
    newIdFurgoneta = request.form.get('idFurgoneta')

    consulta = f"SELECT date, address, idFurgoneta FROM Pedido WHERE id = \'{idPedido}\'"
    pedido = ejecutarConsulta(consulta)

    consulta = f"SELECT id FROM Furgoneta WHERE id = \'{newIdFurgoneta}\'"
    furgoneta = ejecutarConsulta(consulta)

    if not pedido:
      raise ValueError("Pedido no encontrado")
    elif not furgoneta:
      raise ValueError("Furgoneta no encontrada")
    else:
      currentDate, currentAddress, currentIdFurgoneta = pedido[0]
    
    if newDate:
      currentDate = newDate
    if newAddress:
      currentAddress = newAddress
    if newIdFurgoneta:
      currentIdFurgoneta = newIdFurgoneta

    consulta = f"UPDATE Pedido SET date = \'{currentDate}\', address = \'{currentAddress}\', idFurgoneta = \'{currentIdFurgoneta}\' WHERE id = \'{idPedido}\'"
    ejecutarConsulta(consulta)

    respuesta = 'Pedido modificado correctamente'
  except Exception as error:
    respuesta = f'Error al modificar el pedido: {str(error)}'
  finally:
    return respuesta

@app.route('/Pedido/<int:idPedido>', methods=['DELETE'])
def DeletePedido(idPedido):
  respuesta = ''
  try:
    consulta = f"SELECT * FROM Pedido WHERE id = \'{idPedido}\'"
    pedido = ejecutarConsulta(consulta)
    if not pedido:
      raise ValueError("Pedido no encontrado")
    else:
      consulta = f"DELETE FROM ProductoEnPedido WHERE idPedido = \'{idPedido}\'"
      ejecutarConsulta(consulta)

      consulta = f"DELETE FROM Pedido WHERE id = \'{idPedido}\'"
      ejecutarConsulta(consulta)

    respuesta = 'Pedido eliminado correctamente'
  except Exception as error:
    respuesta = f'Error al eliminar el pedido: {str(error)}'
  finally:
    return respuesta
