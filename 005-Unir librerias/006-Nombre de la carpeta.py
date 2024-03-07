import tkinter as tk
from tkinter import filedialog
import os

def carpetaorigen():
    vorigen = filedialog.askdirectory(title="Selecciona carpeta")
    solocarpeta = os.path.basename(vorigen)
    nombrecarpeta.config(text=solocarpeta)

ventana = tk.Tk()
ventana.title("Mejorador de imagenes v0.1 Jose Vicente Carratala")
ventana.geometry("600x400")

tk.Label(ventana,text="Selecciona una carpeta:").pack(padx=20,pady=20)
tk.Button(ventana,text="Seleccionar...",command=carpetaorigen).pack(padx=20,pady=20)
nombrecarpeta = tk.Label(ventana,text="Carpeta:")
nombrecarpeta.pack(padx=20,pady=20)
ventana.mainloop()
