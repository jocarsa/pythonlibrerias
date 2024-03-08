# pip install flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():  
    return render_template('index.html')

@app.route('/sobremi')
def sobremi():  
    return render_template('sobremi.html')

@app.route('/contacto')
def contacto():  
    return render_template('contacto.html')

app.run(debug=True,port=80)


