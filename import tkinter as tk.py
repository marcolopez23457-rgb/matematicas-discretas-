import tkinter as tk
from tkinter import messagebox

# ---------- GENERAR RELACIÓN ----------
def generar_relacion(conjunto):
    relacion = set()
    for a in conjunto:
        for b in conjunto:
            relacion.add((a, b))
    return relacion

# ---------- PROPIEDADES ----------
def es_reflexiva(conjunto, relacion):
    for e in conjunto:
        if (e, e) not in relacion:
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

# ---------- ANALIZAR ----------
def analizar():
    try:
        conjunto = entrada_conjunto.get().split(",")
        conjunto = [x.strip() for x in conjunto]

        if len(conjunto) == 0:
            raise ValueError

        relacion = generar_relacion(conjunto)

        resultado = "Relación generada:\n\n"

        for par in relacion:
            resultado += f"{par} "

        resultado += "\n\nPropiedades:\n"

        if es_reflexiva(conjunto, relacion):
            resultado += "✔ Reflexiva\n"
        else:
            resultado += "✘ No reflexiva\n"

        if es_simetrica(relacion):
            resultado += "✔ Simétrica\n"
        else:
            resultado += "✘ No simétrica\n"

        if es_transitiva(relacion):
            resultado += "✔ Transitiva\n"
        else:
            resultado += "✘ No transitiva\n"

        resultado_label.config(text=resultado)

    except:
        messagebox.showerror("Error","Introduce el conjunto correctamente.\nEjemplo: a,b,c")

# ---------- LIMPIAR ----------
def limpiar():
    entrada_conjunto.delete(0, tk.END)
    resultado_label.config(text="")

# ---------- VENTANA ----------
ventana = tk.Tk()
ventana.title("Analizador de Relaciones")
ventana.geometry("520x450")
ventana.config(bg="#1f1f2e")

titulo = tk.Label(
    ventana,
    text="Analizador de Relaciones Matemáticas",
    font=("Arial",16,"bold"),
    bg="#1f1f2e",
    fg="white"
)
titulo.pack(pady=15)

frame = tk.Frame(ventana,bg="#2f2f45",padx=20,pady=20)
frame.pack()

tk.Label(
    frame,
    text="Ingresa el conjunto (ejemplo: a,b,c o 1,2,3)",
    bg="#2f2f45",
    fg="white",
    font=("Arial",11)
).pack()

entrada_conjunto = tk.Entry(frame,width=30,font=("Arial",12))
entrada_conjunto.pack(pady=10)

frame_botones = tk.Frame(ventana,bg="#1f1f2e")
frame_botones.pack(pady=10)

btn_analizar = tk.Button(
    frame_botones,
    text="Generar y Analizar",
    command=analizar,
    bg="#4CAF50",
    fg="white",
    width=16,
    font=("Arial",11,"bold")
)
btn_analizar.grid(row=0,column=0,padx=10)

btn_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    command=limpiar,
    bg="#e53935",
    fg="white",
    width=16,
    font=("Arial",11,"bold")
)
btn_limpiar.grid(row=0,column=1,padx=10)

resultado_label = tk.Label(
    ventana,
    text="",
    font=("Arial",11),
    bg="#1f1f2e",
    fg="white",
    justify="left",
    wraplength=480
)
resultado_label.pack(pady=20)

ventana.mainloop()