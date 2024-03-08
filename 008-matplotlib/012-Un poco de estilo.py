import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from ttkbootstrap import Style

def grafica():
    directorio = filedialog.askdirectory(title="Selecciona carpeta", initialdir=os.getcwd())

    tamaños = []
    nombres = []

    for archivo in os.listdir(directorio):
        ruta = os.path.join(directorio, archivo)
        if os.path.isfile(ruta):  # Check if it's a file and not a directory
            nombres.append(archivo)  # Use only the file name, not full path
            tamaños.append(os.path.getsize(ruta))

    fig, ax = plt.subplots()
    ax.pie(tamaños, labels=nombres, autopct='%1.1f%%')
    ax.set_title('Pie Chart')

    canvas = FigureCanvasTkAgg(fig, master=marco)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

ventana = tk.Tk()
style = Style(theme="litera")
ventana.geometry("800x800")

marco = ttk.Frame(ventana)
marco.pack(padx=10, pady=10)

tk.Label(ventana,text="Selecciona una carpeta...").pack(padx=10,pady=10)
tk.Button(ventana,text="Pulsa para seleccionar",command=grafica).pack(padx=10,pady=10)

ventana.mainloop()
