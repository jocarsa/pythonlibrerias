from PIL import Image
import random
import tkinter as tk
from tkinter import filedialog

def procesa():
    imagen = Image.open(entrada.get())
    pixeles = imagen.load()
    altura,anchura = imagen.size
    for x in range(0,anchura):
        for y in range(0,altura):
            rojo = pixeles[x,y][0]
            pixeles[x,y] = (rojo,rojo,rojo)
    imagen.save(salida.get())
def origen():
    archivo = filedialog.askopenfilename(title="Selecciona archivos")
    print(archivo)
 
ventana = tk.Tk()

tk.Label(ventana,text="Introduce la imagen:").pack(padx=20,pady=20)
entrada = tk.Button(ventana,text="Selecciona imagen de origen",command=origen)
entrada.pack(padx=20,pady=20)
tk.Label(ventana,text="Introduce el destino:").pack(padx=20,pady=20)
salida = tk.Entry(ventana)
salida.pack(padx=20,pady=20)
tk.Button(ventana,text="Comenzar",command=procesa).pack(padx=20,pady=20)


ventana.mainloop()
