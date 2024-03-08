import os
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def grafica():
    directorio = filedialog.askdirectory(title="Selecciona carpeta", initialdir=os.getcwd())

    tamaños = []
    nombres = []

    for archivo in os.listdir(directorio):
        ruta = os.path.join(directorio, archivo)
        if os.path.isfile(ruta):  # Check if it's a file and not a directory
            nombres.append(ruta)
            tamaños.append(os.path.getsize(ruta))

    plt.pie(tamaños, labels=nombres, autopct='%1.1f%%')

    plt.show()

ventana = tk.Tk()

tk.Label(ventana,text="Selecciona una carpeta...").pack(padx=10,pady=10)
tk.Button(ventana,text="Pulsa para seleccionar",command=grafica).pack(padx=10,pady=10)

ventana.mainloop()
