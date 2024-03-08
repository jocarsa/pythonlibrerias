import matplotlib.pyplot as plt

sizes = [30, 20, 15, 35]
labels = ['Valencia', 'Madrid', 'Barcelona', 'Bilbao']

def onclick(event, labels):
    print(event)

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['red', 'orange', 'yellow', 'black'])

fig.canvas.mpl_connect('button_press_event', lambda event: onclick(event, labels))
plt.show()
