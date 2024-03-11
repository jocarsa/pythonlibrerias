import tkinter as tk
from tkinter import ttk
import mysql.connector

def actualiza():
    pass
    arbol.delete(*arbol.get_children())


conexion = mysql.connector.connect(
    host="localhost",
    user="programagestion",
    password="programagestion",
    database="programagestion"
)

ventana = tk.Tk()
ventana.geometry("800x800")

arbol = ttk.Treeview()
arbol.pack(padx=50,pady=50)

boton = tk.Button(ventana,text="Pulsa",command=actualiza)
boton.pack(padx=50,pady=50)

arbol["columns"] = ("1", "2", "3")

arbol.heading("#0", text="Identificador")
arbol.heading("1", text="Nombre")
arbol.heading("2", text="Email")
arbol.heading("3", text="Teléfono")

cursor = conexion.cursor()
cursor.execute("SELECT * FROM clientes")

registros = cursor.fetchall()

for tupla in registros:
    arbol.insert("", tk.END, text=tupla[0], values=(tupla[1], tupla[2], tupla[3]))

ventana.mainloop()
