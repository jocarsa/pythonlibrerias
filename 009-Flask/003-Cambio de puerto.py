# pip install flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hola mundo desde Flask otra vez que tal'

app.run(debug=True,port=80)


