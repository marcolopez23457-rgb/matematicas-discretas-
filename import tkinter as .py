import tkinter as tk
from tkinter import messagebox

def es_reflexiva(conjunto, relacion):
    for elemento in conjunto:
        if (elemento, elemento) not in relacion:
            return False
    return True

def es_simetrica(relacion):
    for (a, b) in relacion:
        if (b, a) not in relacion:
            return False
    return True

def es_transitiva(relacion):
    for (a, b) in relacion:
        for (c, d) in relacion:
            if b == c and (a, d) not in relacion:
                return False
    return True

def analizar():
    try:
        conjunto = entrada_conjunto.get().split(",")
        conjunto = [x.strip() for x in conjunto]

        pares = entrada_relacion.get().split(";")
        relacion = set()

        for par in pares:
            a, b = par.split(",")
            relacion.add((a.strip(), b.strip()))

        resultado = ""

        if es_reflexiva(conjunto, relacion):
            resultado += "La relación ES reflexiva\n"
        else:
            resultado += "La relación NO es reflexiva\n"

        if es_simetrica(relacion):
            resultado += "La relación ES simétrica\n"
        else:
            resultado += "La relación NO es simétrica\n"

        if es_transitiva(relacion):
            resultado += "La relación ES transitiva\n"
        else:
            resultado += "La relación NO es transitiva\n"

        label_resultado.config(text=resultado)

    except:
        messagebox.showerror("Error", "Verifica el formato de los datos")

# Ventana principal
ventana = tk.Tk()
ventana.title("Analizador de Relaciones")
ventana.geometry("400x300")

# Conjunto
tk.Label(ventana, text="Conjunto (separado por comas):").pack()
entrada_conjunto = tk.Entry(ventana, width=40)
entrada_conjunto.pack()

# Relación
tk.Label(ventana, text="Relación (ej: 1,1;1,2;2,1):").pack()
entrada_relacion = tk.Entry(ventana, width=40)
entrada_relacion.pack()

# Botón
tk.Button(ventana, text="Analizar Relación", command=analizar).pack(pady=10)

# Resultado
label_resultado = tk.Label(ventana, text="", justify="left")
label_resultado.pack()

ventana.mainloop()