import tkinter as tk
from tkinter import messagebox


class ConversorDecimalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor Decimal a Binario")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        # Título
        self.titulo = tk.Label(
            root,
            text="Conversor Decimal a Binario",
            font=("Arial", 16, "bold")
        )
        self.titulo.pack(pady=10)

        # Campo de entrada
        self.label_input = tk.Label(root, text="Ingresa un número decimal:")
        self.label_input.pack()

        self.entry_decimal = tk.Entry(root, width=30)
        self.entry_decimal.pack(pady=5)

        # Botones
        self.btn_convertir = tk.Button(
            root,
            text="Convertir",
            command=self.convertir
        )
        self.btn_convertir.pack(pady=5)

        self.btn_limpiar = tk.Button(
            root,
            text="Limpiar",
            command=self.limpiar
        )
        self.btn_limpiar.pack()

        # Resultado
        self.label_resultado = tk.Label(
            root,
            text="Resultado: ",
            font=("Arial", 12)
        )
        self.label_resultado.pack(pady=15)

    def convertir(self):
        decimal = self.entry_decimal.get().strip()

        if not decimal:
            messagebox.showwarning("Advertencia", "Debes ingresar un número.")
            return

        if not decimal.isdigit():
            messagebox.showerror("Error", "Debes ingresar un número decimal válido (solo números positivos).")
            return

        numero = int(decimal)
        binario = bin(numero)[2:]  # quitamos el prefijo '0b'
        self.label_resultado.config(text=f"Resultado: {binario}")

    def limpiar(self):
        self.entry_decimal.delete(0, tk.END)
        self.label_resultado.config(text="Resultado: ")


def main():
    root = tk.Tk()
    app = ConversorDecimalApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
