# pip install flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hola mundo desde Flask'

if __name__ == '__main__':
    app.run(debug=True)


