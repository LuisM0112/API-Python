from flask import request
from main import app, ejecutarConsulta

# Devuelve una lista de Furgonetas
@app.route('/Furgonetas', methods=['GET'])
def GetListaFurgonetas():
    
  consulta = 'SELECT * FROM Furgoneta'
  respuesta = ejecutarConsulta(consulta)

  return respuesta

@app.route('/Furgoneta/<string:matricula>', methods=['GET'])
def GetFurgonetaByMatricula(matricula):
  consulta = f'SELECT * FROM Furgoneta WHERE Furgoneta.matricula = \'{matricula}\''
  respuesta = ejecutarConsulta(consulta)

  return respuesta

@app.route('/Furgoneta', methods=['POST'])
def PostFurgoneta():
  respuesta = ''
  try:

    matricula = request.form['matricula']
    marca = request.form['marca']
    modelo = request.form['modelo']

    consulta = f'INSERT INTO Furgoneta (matricula, marca, modelo, idFurgoneta) VALUES (\'{matricula}\', \'{marca}\', \'{modelo}\')'
    respuesta = ejecutarConsulta(consulta)

    respuesta = 'Furgoneta creada correctamente'
  except Exception as error:
    respuesta = f'Error al crear la furgoneta: {str(error)}'
  finally:
    return respuesta

@app.route('/Furgoneta/<int:idFurgoneta>', methods=['PUT'])
def PutFurgoneta(idFurgoneta):
  respuesta = ''
  try:
    nueva_marca = request.form.get('marca')
    nuevo_modelo = request.form.get('modelo')
    nueva_idFurgoneta = request.form.get('idFurgoneta')

    consulta = f"SELECT marca, modelo, idFurgoneta FROM Furgoneta WHERE idFurgoneta = \'{idFurgoneta}\'"
    furgoneta = ejecutarConsulta(consulta)
    if not furgoneta:
      raise ValueError("Furgoneta no encontrada")
    else:
      marca_actual, modelo_actual, idFurgoneta_actual = furgoneta[0]

    if nueva_marca:
      marca_actual = nueva_marca
    if nuevo_modelo:
      modelo_actual = nuevo_modelo
    if nueva_idFurgoneta:
      idFurgoneta_actual = nueva_idFurgoneta

    consulta = f"UPDATE Furgoneta SET marca = \'{marca_actual}\', modelo = \'{modelo_actual}\', idFurgoneta = \'{idFurgoneta_actual}\' WHERE idFurgoneta = \'{idFurgoneta}\'"
    ejecutarConsulta(consulta)

    respuesta = 'Furgoneta modificada correctamente'
  except Exception as error:
    respuesta = f'Error al modificar la furgoneta: {str(error)}'
  finally:
    return respuesta

@app.route('/Furgoneta/<int:idFurgoneta>', methods=['DELETE'])
def DeleteFurgoneta(idFurgoneta):
  respuesta = ''
  try:
    consulta = f"SELECT * FROM Furgoneta WHERE idFurgoneta = \'{idFurgoneta}\'"
    furgoneta = ejecutarConsulta(consulta)

    if not furgoneta:
      raise ValueError("Furgoneta no encontrada")
    else:
      consulta = f"DELETE FROM Furgoneta WHERE idFurgoneta = \'{idFurgoneta}\'"
      ejecutarConsulta(consulta)

    respuesta = 'Furgoneta eliminada correctamente'
  except Exception as error:
    respuesta = f'Error al eliminar la furgoneta: {str(error)}'
  finally:
    return respuesta
