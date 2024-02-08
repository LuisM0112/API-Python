from statistics import variance
from flask import Flask


app = Flask(__name__)

def Espanol():
    español = "<p>Hola, Mundo!</p>"
    return español

@app.route("/")
def hello_world(): 
   
    return  Espanol()+"<p>Hello, World!</p>"
   

@app.route("/returnList")
def ReturnList():
    resultado = "hola"
    return "<p>"+resultado+"</p>"
    
