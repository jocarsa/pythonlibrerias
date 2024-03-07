import tkinter as tk
from tkinter import filedialog
import os

def carpetaorigen():
    vorigen = filedialog.askdirectory(title="Selecciona carpeta")
    solocarpeta = os.path.basename(vorigen)
    nombrecarpeta.config(text=solocarpeta)

def carpetadestino():
    vdestino = filedialog.askdirectory(title="Selecciona carpeta")
    solocarpeta = os.path.basename(vdestino)
    nombrecarpetadestino.config(text=solocarpeta)

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
ventana.mainloop()
