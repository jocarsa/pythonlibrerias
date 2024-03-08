# pip install flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():  
    return "Esta es la página de inicio"

@app.route('/sobremi')
def sobremi():  
    return "Esta es la página de sobre mi"

@app.route('/contacto')
def contacto():  
    return "Esta es la página de contacto"

app.run(debug=True,port=80)


