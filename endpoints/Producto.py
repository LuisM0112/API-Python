from flask import abort, request
from main import app, ejecutarConsulta

@app.route("/Productos", methods=['GET'])
def GetListaProductos():
  respuesta = ''
  try:
    consulta = "SELECT * FROM Producto"
    respuesta = ejecutarConsulta(consulta)
  except Exception as error:
    respuesta = f'Error al obtener la lista de pedidos: {str(error)}'
  finally:
    return respuesta

@app.route("/Producto", methods=['POST'])
def CrearProducto():
  respuesta = ''
  try:
    product_name = request.form['name']
    product_description = request.form['description']
    product_stock = request.form['stock']

    if not product_name:
      raise ValueError("Introduce el nombre")
    elif not product_description:
      raise ValueError("Introduce la descripción")
    elif not product_stock or int(product_stock) < 1:
      raise ValueError("Stock no válido")
       
    consulta = f"INSERT INTO Producto (name, description, stock) VALUES (\'{product_name}\', \'{product_description}\', \'{product_stock}\')"
    ejecutarConsulta(consulta)
    respuesta = "Producto creado correctamente"
  except Exception as error:
    respuesta = f'Error al crear el producto: {str(error)}'
  finally:
    return respuesta

@app.route("/Producto/<int:idPedido>", methods=['DELETE'])
def EliminarProducto(idPedido):
  respuesta = ''
  try:
    consulta = f"SELECT * FROM Producto WHERE id = \'{idPedido}\'"
    pedido = ejecutarConsulta(consulta)
    if not pedido:
      raise ValueError("Producto no encontrado")
    else:
      consulta = f"DELETE FROM Producto WHERE id = \'{idPedido}\'"
      ejecutarConsulta(consulta)
      respuesta = "Producto eliminado correctamente"
  except Exception as error:
    respuesta = f'Error al eliminar el producto: {str(error)}'
  finally:
    return respuesta

@app.route("/Producto/<int:idPedido>", methods=['PUT'])
def EditarProducto(idPedido):
  respuesta = ''
  try:
    product_name = request.form["name"]
    product_description = request.form["description"]
    product_stock = request.form['stock']

    consulta = f"SELECT name, description, stock FROM Producto WHERE id = \'{idPedido}\'"
    producto = ejecutarConsulta(consulta)
    if not producto:
      raise ValueError("Producto no encontrado")
    else:
      currentName, currentDescription, currentStock = producto[0]
    
    if product_name:
      currentName = product_name
    if product_description:
      currentDescription = product_description
    if product_stock:
      currentStock = product_stock

    consulta = f"UPDATE Producto SET name = \'{currentName}\', description = \'{currentDescription}\', stock = \'{currentStock}\' WHERE id = \'{idPedido}\'"
    ejecutarConsulta(consulta)

    respuesta = "Producto modificado correctamente"
  except Exception as error:
    respuesta = f'Error al modificar el producto: {str(error)}'
  finally:
    return respuesta


@app.route("/Producto/<int:idPedido>", methods=['GET'])
def GetProductoById(idPedido):
  respuesta = ''
  try:
    consulta = f'SELECT * FROM Producto WHERE id = \'{idPedido}\''
    respuesta = ejecutarConsulta(consulta)
  except Exception as error:
    respuesta = f'Error al obtener la lista de pedidos: {str(error)}'
  finally:
    return respuesta