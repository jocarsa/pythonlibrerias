import tkinter as tk
from tkinter import filedialog

def carpetaorigen():
    vorigen = filedialog.askdirectory(title="Selecciona carpeta")

ventana = tk.Tk()
ventana.title("Mejorador de imagenes v0.1 Jose Vicente Carratala")
ventana.geometry("600x400")

tk.Label(ventana,text="Selecciona una carpeta:").pack(padx=50,pady=50)
tk.Button(ventana,text="Seleccionar...",command=carpetaorigen).pack(padx=50,pady=50)

ventana.mainloop()
