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
  try:
    consulta = f'SELECT * FROM Furgoneta WHERE Furgoneta.matricula = \'{matricula}\''
    respuesta = ejecutarConsulta(consulta)
    if not respuesta:
      raise ValueError("Furgoneta no encontrada")
  except Exception as error:
    respuesta = f'Error al obtener la furgoneta: {str(error)}'
  finally:
    return respuesta

@app.route('/Furgoneta', methods=['POST'])
def PostFurgoneta():
  respuesta = ''
  try:

    matricula = request.form['matricula']
    marca = request.form['marca']

    consulta = f'INSERT INTO Furgoneta (matricula, marca) VALUES (\'{matricula}\', \'{marca}\')'
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
    nueva_matricula = request.form.get('matricula')

    consulta = f"SELECT marca, matricula FROM Furgoneta WHERE id = \'{idFurgoneta}\'"
    furgoneta = ejecutarConsulta(consulta)
    if not furgoneta:
      raise ValueError("Furgoneta no encontrada")
    else:
      marca_actual, matricula_actual = furgoneta[0]

    if nueva_marca:
      marca_actual = nueva_marca
    if nueva_matricula:
      matricula_actual = nueva_matricula

    consulta = f"UPDATE Furgoneta SET marca = \'{marca_actual}\', matricula = \'{matricula_actual}\' WHERE id = \'{idFurgoneta}\'"
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
    consulta = f"SELECT * FROM Furgoneta WHERE id = \'{idFurgoneta}\'"
    furgoneta = ejecutarConsulta(consulta)

    if not furgoneta:
      raise ValueError("Furgoneta no encontrada")
    else:
      consulta = f"DELETE FROM Furgoneta WHERE id = \'{idFurgoneta}\'"
      ejecutarConsulta(consulta)

    respuesta = 'Furgoneta eliminada correctamente'
  except Exception as error:
    respuesta = f'Error al eliminar la furgoneta: {str(error)}'
  finally:
    return respuesta
