# pip install matplotlib
import matplotlib.pyplot as plt


sizes = [30, 20, 15, 35]
labels = ['Valencia', 'Madrid', 'Barcelona', 'Bilbao']

fig = plt.figure(facecolor='blue')

plt.pie(sizes, labels=labels, autopct='%1.1f%%',colors=['red','orange','yellow','black'])

plt.show()
