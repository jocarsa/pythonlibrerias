import tkinter as tk
from tkinter import filedialog
import os

vorigen = 0
vdestino = 0

def carpetaorigen():
    global vorigen
    vorigen = filedialog.askdirectory(title="Selecciona carpeta")
    solocarpeta = os.path.basename(vorigen)
    nombrecarpeta.config(text=solocarpeta)

def carpetadestino():
    global vdestino
    vdestino = filedialog.askdirectory(title="Selecciona carpeta")
    solocarpeta = os.path.basename(vdestino)
    nombrecarpetadestino.config(text=solocarpeta)
def ejecutar():
    global vorigen
    global vdestino
    directorio = vorigen
    for raiz, directorios, archivos in os.walk(directorio):
        for archivo in archivos:
            print(archivo)
    print("vamos a por ello")

ventana = tk.Tk()
ventana.title("Mejorador de imagenes v0.1 Jose Vicente Carratala")
ventana.geometry("600x400")

tk.Label(ventana,text="Selecciona una carpeta:").pack(padx=10,pady=10)
tk.Button(ventana,text="Seleccionar...",command=carpetaorigen).pack(padx=10,pady=10)
nombrecarpeta = tk.Label(ventana,text="Carpeta:")
nombrecarpeta.pack(padx=10,pady=10)
tk.Label(ventana,text="Selecciona una carpeta de destino:").pack(padx=10,pady=10)
tk.Button(ventana,text="Seleccionar...",command=carpetadestino).pack(padx=10,pady=10)
nombrecarpetadestino = tk.Label(ventana,text="Carpeta:")
nombrecarpetadestino.pack(padx=10,pady=10)
tk.Button(ventana,text="Ejecutar",command=ejecutar).pack(padx=10,pady=10)
ventana.mainloop()
