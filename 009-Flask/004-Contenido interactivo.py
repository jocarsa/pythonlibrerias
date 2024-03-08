# pip install flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    cadena = ""
    for dia in range(0,30):
        cadena += "hoy es el dia "+str(dia)+" del mes <br>"
    return cadena

app.run(debug=True,port=80)


