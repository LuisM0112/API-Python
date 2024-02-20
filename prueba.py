import sqlite3

from statistics import variance
from flask import Flask
from flask import request
import sqlite3

nombreBD = "HomeX.db"

app = Flask(__name__)


@app.route("/", methods=['GET'])
def Inicio():
    connection = sqlite3.connect(nombreBD)
    cursor = connection.cursor()
    res = cursor.execute("SELECT id, name, description, stock FROM Producto").fetchall()
    connection.close()
    return str(res)

@app.route("/CrearProducto", methods=['POST'])
def CrearProducto():

    product_name = request.form.get('name')
    product_description = request.form.get('description')
    product_stock = request.form.get('stock')
    connection = sqlite3.connect(nombreBD)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Producto (name, description, stock) VALUES (?, ?, ?)",(product_name, product_description, product_stock))
    connection.commit()
    connection.close()
    return "Producto Creado"

@app.route("/EliminarProducto", methods=['POST'])
def EliminarProducto():
    product_id = request.forms.get('id')
    connection = sqlite3.connect(nombreBD)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Producto WHERE id = "+product_id)
    connection.commit()
    connection.close()
    return "Producto Eliminar"

@app.route("/EditarProducto", methods=['PUT'])
def EditarProducto():
    product_id = request.args.get('id')
    product_name = request.form.get('name')
    product_description = request.form.get('description')
    product_stock = request.form.get('stock')
    connection = sqlite3.connect(nombreBD)
    cursor = connection.cursor()
    cursor.execute("UPDATE Producto SET name = ?, description = ?, stock = ? WHERE id = ?", (product_name, product_description, product_stock, product_id))
    connection.commit()
    connection.close()
    return "Producto Actualizado"


@app.route("/BuscarProducto", methods=['GET'])
def BuscarProducto():
    product_id = request.forms.get('id')
    connection = sqlite3.connect(nombreBD)
    cursor = connection.cursor()
    res = cursor.execute("SELECT name, description, stock FROM Producto WHERE id = ?", (product_id,)).fetchall()
    connection.close()
    return(res)
