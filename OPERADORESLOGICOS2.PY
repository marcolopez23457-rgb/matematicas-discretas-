import tkinter as tk
from tkinter import scrolledtext

# Funciones de compuertas lógicas
def AND(a, b):
    return int(a and b)

def OR(a, b):
    return int(a or b)

def NOT(a):
    return int(not a)

# Función para mostrar las tablas
def mostrar_tablas():
    resultado.delete(1.0, tk.END)

    texto = "TABLA DE VERDAD AND\n"
    texto += "A B | A AND B\n"
    for A in [0,1]:
        for B in [0,1]:
            texto += f"{A} {B} | {AND(A,B)}\n"

    texto += "\nTABLA DE VERDAD OR\n"
    texto += "A B | A OR B\n"
    for A in [0,1]:
        for B in [0,1]:
            texto += f"{A} {B} | {OR(A,B)}\n"

    texto += "\nTABLA DE VERDAD NOT\n"
    texto += "A | NOT A\n"
    for A in [0,1]:
        texto += f"{A} | {NOT(A)}\n"

    resultado.insert(tk.END, texto)

# Crear ventana
ventana = tk.Tk()
ventana.title("Tablas de Verdad - Compuertas Lógicas")
ventana.geometry("400x350")

titulo = tk.Label(ventana, text="Tablas de Verdad", font=("Arial",16))
titulo.pack(pady=10)

boton = tk.Button(ventana, text="Mostrar Tablas", command=mostrar_tablas)
boton.pack(pady=10)

resultado = scrolledtext.ScrolledText(ventana, width=40, height=15)
resultado.pack(pady=10)

ventana.mainloop()