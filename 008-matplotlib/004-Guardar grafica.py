# pip install matplotlib
import matplotlib.pyplot as plt

x = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
y = [254, 345, 243, 545, 345]

plt.bar(x, y)

plt.xlabel('Meses')
plt.ylabel('Cantidades')
plt.title('Facturación')

plt.savefig("migrafica.png")
