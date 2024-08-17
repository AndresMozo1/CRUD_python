import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from FormularioClientes import FormularioClientes
from FormularioProductos import FormularioProductos

class InterfazBienvenida:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Gestión")
        self.ventana.geometry("800x600")  # Ajusta el tamaño según tu imagen

        # Cargar y redimensionar la imagen de fondo
        imagen = Image.open("darden-restaurants-inc.png")
        imagen = imagen.resize((800, 600), Image.LANCZOS)  # Ajusta el tamaño según tu ventana
        self.fondo = ImageTk.PhotoImage(imagen)

        # Crear un canvas y poner la imagen en él
        self.canvas = tk.Canvas(self.ventana, width=1024, height=768)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.fondo, anchor="nw")

        self.crear_interfaz()

    def crear_interfaz(self):
        # Título
        titulo = self.canvas.create_text(400, 50, text="Bienvenido al Sistema de Gestión", 
                                         font=("Arial", 24, "bold"), fill="black")

        # Botón para Clientes
        btn_clientes = tk.Button(self.canvas, text="Gestión de Clientes", command=self.abrir_clientes, 
                                 bg="#4B0082", fg="white", font=("Arial", 12), width=20)
        self.canvas.create_window(400, 150, window=btn_clientes)

        # Botón para Productos
        btn_productos = tk.Button(self.canvas, text="Gestión de Productos", command=self.abrir_productos, 
                                  bg="#008080", fg="white", font=("Arial", 12), width=20)
        self.canvas.create_window(400, 220, window=btn_productos)

        # Botón para Salir
        btn_salir = tk.Button(self.canvas, text="Salir", command=self.ventana.quit, 
                              bg="#B22222", fg="white", font=("Arial", 12), width=20)
        self.canvas.create_window(400, 290, window=btn_salir)

    def abrir_clientes(self):
        formulario_clientes = FormularioClientes()
        self.ventana.wait_window(formulario_clientes.base)

    def abrir_productos(self):
        formulario_productos = FormularioProductos()
        self.ventana.wait_window(formulario_productos.base)

    def iniciar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = InterfazBienvenida()
    app.iniciar()