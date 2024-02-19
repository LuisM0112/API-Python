from flask import request
from main import app, ejecutarConsulta

@app.route('/ProductoEnPedido/<int:idPedido>', methods=['GET'])
def GetListaProductoEnPedido(idPedido):
  respuesta = ''
  try:
    consulta = f'SELECT * FROM Pedido WHERE id = {idPedido}'
    pedido = ejecutarConsulta(consulta)

    if not pedido:
      raise ValueError("Pedido no encontrado")
    else:
      consulta = f'SELECT * FROM ProductoEnPedido WHERE idPedido = {idPedido}'
      respuesta = ejecutarConsulta(consulta)

  except Exception as error:
    respuesta = f'Error al obtener la lista de pedidos: {str(error)}'
  finally:
    return respuesta

@app.route('/ProductoEnPedido/<int:idPedido>', methods=['POST'])
def PostProductoEnPedido(idPedido):
  respuesta = ''
  try:
    idProducto = request.form.get('idProducto')
    cantidad = request.form.get('cantidad')

    consulta = f"SELECT * FROM Pedido WHERE id = \'{idPedido}\'"
    pedido = ejecutarConsulta(consulta)

    consulta = f"SELECT * FROM Producto WHERE id = \'{idProducto}\'"
    producto = ejecutarConsulta(consulta)
    print(producto)

    if not pedido:
      raise ValueError("Pedido no encontrado")
    elif not producto:
      raise ValueError("Producto no encontrado")
    elif not cantidad or int(cantidad) < 1:
      raise ValueError("Cantidad no válida")
    else:
      consulta = f"INSERT INTO ProductoEnPedido (idPedido, idProducto, cantidad) VALUES (\'{idPedido}\', \'{idProducto}\', \'{cantidad}\')"
      ejecutarConsulta(consulta)

    respuesta = 'Producto añadido al pedido correctamente'
  except Exception as error:
    respuesta = f'Error al añadir producto al pedido: {str(error)}'
  finally:
    return respuesta

@app.route('/ProductoEnPedido/<int:idPedido>', methods=['PUT'])
def PutProductoEnPedido(idPedido):
  respuesta = ''
  try:
    idProducto = request.form.get('idProducto')
    cantidad = request.form.get('Cantidad')

    consulta = f"SELECT * FROM Pedido WHERE id = \'{idPedido}\'"
    pedido = ejecutarConsulta(consulta)
    if not pedido:
      raise ValueError("Pedido no encontrado")
    elif not idProducto:
      raise ValueError("Producto no encontrado")
    else:
      consulta = f"UPDATE ProductoEnPedido SET cantidad = \'{cantidad}\' WHERE idPedido = \'{idPedido}\' AND idProducto = \'{idProducto}\'"
      pedido = ejecutarConsulta(consulta)

    respuesta = 'Producto del pedido modificado correctamente'
  except Exception as error:
    respuesta = f'Error al modificar el procuto del pedido: {str(error)}'
  finally:
    return respuesta

@app.route('/ProductoEnPedido/<int:idPedido>', methods=['DELETE'])
def DeleteProductoEnPedido(idPedido):
  respuesta = ''
  try:
    idProducto = request.form.get('idProducto')

    consulta = f"SELECT * FROM Pedido WHERE id = \'{idPedido}\'"
    pedido = ejecutarConsulta(consulta)
    
    if not pedido:
      raise ValueError("Pedido no encontrado")
    elif not idProducto:
      raise ValueError("Producto no encontrado")
    else:
      consulta = f"DELETE FROM ProductoEnPedido WHERE idPedido = \'{idPedido}\' AND idProducto = \'{idProducto}\'"
      ejecutarConsulta(consulta)

    respuesta = 'Producto eliminado correctamente del pedido'
  except Exception as error:
    respuesta = f'Error al eliminar el procuto del pedido: {str(error)}'
  finally:
    return respuesta
