import sqlite3

from statistics import variance
from flask import Flask
import sqlite3

nombreBD = "HomeX.db"
# sentenciaTabla = "CREATE TABLE empleado(name, job)"

# Se conecta a la base de datos, si no existe la crea
connection = sqlite3.connect(nombreBD)

# Crea un cursor para poder ejecutar sentencias SQLite
cursor = connection.cursor()

#Crea la entidad para la base de datos
# cursor.execute(sentenciaTabla)
[]
res = cursor.execute("SELECT name FROM Producto")
app = Flask(__name__)


@app.route("/")

def hello_world():

    return "res"