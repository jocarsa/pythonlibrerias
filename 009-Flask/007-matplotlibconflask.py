# pip install flask
from flask import Flask, render_template
import matplotlib.pyplot as plt

app = Flask(__name__)

x = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
y = [254, 345, 243, 545, 345]

plt.bar(x, y)

plt.xlabel('Meses')
plt.ylabel('Cantidades')
plt.title('Facturación')

plt.savefig("static/grafica.png")


@app.route('/')
def inicio():  
    return render_template('index.html')


app.run(debug=True,port=80)


