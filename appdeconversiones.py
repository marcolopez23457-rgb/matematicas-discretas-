import tkinter as tk
from tkinter import ttk, messagebox


class ConversorApp:

    COLOR_FONDO = "#1e1e2f"
    COLOR_BOTON = "#4CAF50"
    COLOR_TEXTO = "white"
    COLOR_RESULTADO = "#2e2e3e"

    def __init__(self, root):
        self.root = root
        self.root.title("🔢 Conversor de Sistemas Numéricos")
        self.root.geometry("500x450")
        self.root.configure(bg=self.COLOR_FONDO)
        self.root.resizable(False, False)

        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")

        self.crear_menu()
        self.crear_interfaz_principal()

    # =========================
    # MENÚ
    # =========================
    def crear_menu(self):
        barra_menu = tk.Menu(self.root, bg="#2b2b40", fg="white")

        menu_archivo = tk.Menu(barra_menu, tearoff=0,
                               bg="#2b2b40", fg="white")

        menu_archivo.add_command(label="🔄 Reiniciar",
                                 command=self.reiniciar_app)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="❌ Salir",
                                 command=self.root.quit)

        barra_menu.add_cascade(label="📁 Archivo", menu=menu_archivo)
        self.root.config(menu=barra_menu)

    # =========================
    # INTERFAZ PRINCIPAL
    # =========================
    def crear_interfaz_principal(self):

        titulo = tk.Label(
            self.root,
            text="CONVERSOR DE SISTEMAS NUMÉRICOS",
            font=("Arial", 16, "bold"),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_TEXTO
        )
        titulo.pack(pady=20)

        descripcion = tk.Label(
            self.root,
            text="Selecciona el tipo de conversión:",
            font=("Arial", 11),
            bg=self.COLOR_FONDO,
            fg="lightgray"
        )
        descripcion.pack(pady=10)

        frame_botones = tk.Frame(self.root, bg=self.COLOR_FONDO)
        frame_botones.pack(pady=20)

        self.crear_boton(frame_botones,
                         "🔟 Decimal → Binario",
                         self.ventana_decimal_binario)

        self.crear_boton(frame_botones,
                         "🅰 Hexadecimal → Octal",
                         self.ventana_hex_octal)

        self.crear_boton(frame_botones,
                         "🧮 Octal → Hexadecimal",
                         self.ventana_octal_hex)

        self.crear_boton(frame_botones,
                         "💻 Binario → Decimal",
                         self.ventana_binario_decimal)

    def crear_boton(self, parent, texto, comando):
        boton = tk.Button(
            parent,
            text=texto,
            command=comando,
            width=30,
            height=2,
            bg=self.COLOR_BOTON,
            fg="white",
            font=("Arial", 11, "bold"),
            bd=0,
            cursor="hand2"
        )
        boton.pack(pady=8)

    # =========================
    # VENTANAS
    # =========================
    def crear_ventana_conversion(self, titulo, funcion_conversion):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        ventana.geometry("400x300")
        ventana.configure(bg=self.COLOR_FONDO)
        ventana.resizable(False, False)

        tk.Label(
            ventana,
            text=titulo,
            font=("Arial", 14, "bold"),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_TEXTO
        ).pack(pady=15)

        tk.Label(
            ventana,
            text="Ingresa el número:",
            bg=self.COLOR_FONDO,
            fg="lightgray"
        ).pack()

        entrada = tk.Entry(ventana, width=25, font=("Arial", 12))
        entrada.pack(pady=10)

        resultado_frame = tk.Frame(
            ventana,
            bg=self.COLOR_RESULTADO,
            width=300,
            height=50
        )
        resultado_frame.pack(pady=15)

        resultado_label = tk.Label(
            resultado_frame,
            text="Resultado aparecerá aquí",
            bg=self.COLOR_RESULTADO,
            fg="white",
            font=("Arial", 12)
        )
        resultado_label.pack(pady=10)

        def ejecutar_conversion():
            numero = entrada.get().strip()
            if not numero:
                messagebox.showwarning("Campo vacío",
                                       "Por favor ingresa un número.")
                return
            try:
                resultado = funcion_conversion(numero)
                resultado_label.config(text=f"Resultado: {resultado}")
            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Número inválido para esta conversión."
                )

        tk.Button(
            ventana,
            text="Convertir",
            command=ejecutar_conversion,
            bg=self.COLOR_BOTON,
            fg="white",
            font=("Arial", 11, "bold"),
            width=15,
            cursor="hand2"
        ).pack(pady=5)

    # =========================
    # FUNCIONES DE CONVERSIÓN
    # =========================
    @staticmethod
    def convertir_decimal_binario(numero):
        return bin(int(numero))[2:]

    @staticmethod
    def convertir_hex_octal(numero):
        decimal = int(numero, 16)
        return oct(decimal)[2:]

    @staticmethod
    def convertir_octal_hex(numero):
        decimal = int(numero, 8)
        return hex(decimal)[2:].upper()

    @staticmethod
    def convertir_binario_decimal(numero):
        return str(int(numero, 2))

    # =========================
    # MÉTODOS DE VENTANAS
    # =========================
    def ventana_decimal_binario(self):
        self.crear_ventana_conversion(
            "🔟 Decimal → Binario",
            self.convertir_decimal_binario
        )

    def ventana_hex_octal(self):
        self.crear_ventana_conversion(
            "🅰 Hexadecimal → Octal",
            self.convertir_hex_octal
        )

    def ventana_octal_hex(self):
        self.crear_ventana_conversion(
            "🧮 Octal → Hexadecimal",
            self.convertir_octal_hex
        )

    def ventana_binario_decimal(self):
        self.crear_ventana_conversion(
            "💻 Binario → Decimal",
            self.convertir_binario_decimal
        )

    # =========================
    # EXTRA
    # =========================
    def reiniciar_app(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.crear_interfaz_principal()


# =========================
# EJECUTAR
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorApp(root)
    root.mainloop()
