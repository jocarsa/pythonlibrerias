import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
from PIL import Image
from ttkbootstrap import Style
from PIL import Image, ImageTk

vorigen = 0
vdestino = 0
def gris(pixeles,anchura,altura):
    for x in range(0,anchura):
        for y in range(0,altura):
            rojo = pixeles[x,y][0]
            pixeles[x,y] = (rojo,rojo,rojo)
    return pixeles

def umbral(pixeles,anchura,altura):
    for x in range(0,anchura):
        for y in range(0,altura):
            rojo = pixeles[x,y][0]
            if rojo < 127:
                pixeles[x,y] = (0,0,0)
            else:
                pixeles[x,y] = (255,255,255)
    return pixeles
    
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
    print(selector.get())
    global vorigen
    global vdestino
    directorio = vorigen
    for raiz, directorios, archivos in os.walk(directorio):
        print(f"Hay {len(archivos)} archivos en la carpeta")
        numerodearchivos = len(archivos)
        contador = 0
        for archivo in archivos:
            try:
                print(os.path.join(raiz, archivo))
                imagen = Image.open(os.path.join(raiz, archivo))
                pixeles = imagen.load()
                anchura,altura = imagen.size   
                if selector.get() == "grises":
                    pixeles = gris(pixeles,anchura,altura)
                elif selector.get() == "umbral":
                    pixeles = umbral(pixeles,anchura,altura)
                imagen.save(os.path.join(vdestino, archivo))
            except Exception as e:
                print("ha ocurrido algun error",e)
            barra.config(value=((contador/numerodearchivos)*100))
            ventana.update_idletasks()
            contador += 1
            
    print("vamos a por ello")

ventana = tk.Tk()
style = Style(theme="litera")
ventana.title("Mejorador de imagenes v0.1 Jose Vicente Carratala")
ventana.geometry("500x500")

logo = Image.open("logo.png")
foto =ImageTk.PhotoImage(logo)
tk.Label(ventana,image=foto).pack(padx=10,pady=10)

tk.Label(ventana,text="Selecciona una carpeta:").pack(padx=10,pady=10)
tk.Button(ventana,text="Seleccionar...",command=carpetaorigen).pack(padx=10,pady=10)
nombrecarpeta = tk.Label(ventana,text="Carpeta:")
nombrecarpeta.pack(padx=10,pady=10)
tk.Label(ventana,text="Selecciona una carpeta de destino:").pack(padx=10,pady=10)
tk.Button(ventana,text="Seleccionar...",command=carpetadestino).pack(padx=10,pady=10)
nombrecarpetadestino = tk.Label(ventana,text="Carpeta:")
nombrecarpetadestino.pack(padx=10,pady=10)
selector = ttk.Combobox(ventana,values=['grises','umbral'])
selector.pack(padx=10,pady=10)
tk.Button(ventana,text="Ejecutar",command=ejecutar).pack(padx=10,pady=10)
barra = ttk.Progressbar(ventana,value=0)
barra.pack(padx=10,pady=10)
ventana.mainloop()
