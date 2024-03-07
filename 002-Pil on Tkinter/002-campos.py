from PIL import Image
import random
import tkinter as tk

imagen = Image.open("josevicente.jpg")
print(imagen)
pixeles = imagen.load()

altura,anchura = imagen.size
for x in range(0,anchura):
    for y in range(0,altura):
        rojo = pixeles[x,y][0]
        verde = pixeles[x,y][1]
        azul = pixeles[x,y][2]
        promedio = round((rojo+verde+azul)/3)
        if promedio < 127:
            pixeles[x,y] = (0,0,0)
        else:
            pixeles[x,y] = (255,255,255)

def procesa():
    pass
 
ventana = tk.Tk()

tk.Label(ventana,text="Introduce la imagen:").pack(padx=20,pady=20)
entrada = tk.Entry(ventana)
entrada.pack(padx=20,pady=20)
tk.Label(ventana,text="Introduce el destino:").pack(padx=20,pady=20)
salida = tk.Entry(ventana)
salida.pack(padx=20,pady=20)
tk.Button(ventana,text="Comenzar",command=procesa).pack(padx=20,pady=20)


ventana.mainloop()
