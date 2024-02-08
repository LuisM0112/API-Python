import sqlite3

from statistics import variance
from flask import Flask


app = Flask(__name__)

con = sqlite3.connect("Homex.db")

cur = con.cursor()

res =  cur.execute("SELECT name FROM Producto")

print(res)
