import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Clientes import CClientes  # Importando las clases necesarias
from Productos import CProductos

# Encapsular la lógica en clases
class FormularioBase:
    def __init__(self, title, bg_color, campos, obtener_datos, insertar_datos, modificar_datos, eliminar_datos):
        self.base = Tk()
        self.base.geometry("1200x300")
        self.base.title(title)
        self.base.configure(bg=bg_color)

        self.campos = campos
        self.obtener_datos = obtener_datos
        self.insertar_datos = insertar_datos
        self.modificar_datos = modificar_datos
        self.eliminar_datos = eliminar_datos
        self.entries = {}

        self.create_ui(bg_color)
        self.actualizar_treeview()

        self.base.mainloop()

    def create_ui(self, bg_color):
        groupBox = LabelFrame(self.base, text="Datos", padx=5, pady=5, bg=bg_color, fg="white")
        groupBox.grid(row=0, column=0, padx=10, pady=10)

        for idx, campo in enumerate(self.campos):
            Label(groupBox, text=f"{campo}:", width=13, font=("arial", 12), bg=bg_color, fg="white").grid(row=idx, column=0)
            self.entries[campo] = Entry(groupBox)
            self.entries[campo].grid(row=idx, column=1)

        # Botones
        Button(groupBox, text="Guardar", width=10, command=self.guardar_registro, bg="#F2E8C6").grid(row=len(self.campos), column=0)
        Button(groupBox, text="Modificar", width=10, command=self.modificar_registro, bg="#F2E8C6").grid(row=len(self.campos), column=1)
        Button(groupBox, text="Eliminar", width=10, command=self.eliminar_registro, bg="#F2E8C6").grid(row=len(self.campos), column=2)

        # Treeview
        groupBox = LabelFrame(self.base, text="Lista", padx=5, pady=5, bg=bg_color, fg="white")
        groupBox.grid(row=0, column=1, padx=5, pady=5)

        self.tree = ttk.Treeview(groupBox, columns=self.campos, show='headings', height=5)
        for idx, campo in enumerate(self.campos):
            self.tree.column(f"# {idx+1}", anchor=CENTER)
            self.tree.heading(f"# {idx+1}", text=campo)

        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_registro)
        self.tree.pack()

    def guardar_registro(self):
        try:
            datos = [entry.get() for entry in self.entries.values()]
            self.insertar_datos(*datos)
            messagebox.showinfo("Información", "Los datos fueron guardados")
            self.limpiar_entries()
            self.actualizar_treeview()
        except Exception as error:
            messagebox.showerror("Error", f"Error al guardar el registro: {error}")

    def modificar_registro(self):
        try:
            datos = [entry.get() for entry in self.entries.values()]
            self.modificar_datos(*datos)
            messagebox.showinfo("Información", "Los datos fueron actualizados")
            self.limpiar_entries()
            self.actualizar_treeview()
        except Exception as error:
            messagebox.showerror("Error", f"Error al modificar el registro: {error}")

    def eliminar_registro(self):
        try:
            id_usuario = self.entries[self.campos[0]].get()  # Asumiendo que el primer campo es el ID
            self.eliminar_datos(id_usuario)
            messagebox.showinfo("Información", "Los datos fueron eliminados")
            self.limpiar_entries()
            self.actualizar_treeview()
        except Exception as error:
            messagebox.showerror("Error", f"Error al eliminar el registro: {error}")

    def seleccionar_registro(self, event):
        try:
            item_seleccionado = self.tree.focus()
            if item_seleccionado:
                values = self.tree.item(item_seleccionado)['values']
                for idx, value in enumerate(values):
                    self.entries[self.campos[idx]].delete(0, END)
                    self.entries[self.campos[idx]].insert(0, value)
        except Exception as error:
            messagebox.showerror("Error", f"Error al seleccionar el registro: {error}")

    def actualizar_treeview(self):
        try:
            self.tree.delete(*self.tree.get_children())
            datos = self.obtener_datos()
            for row in datos:
                self.tree.insert("", "end", values=row)
        except Exception as error:
            messagebox.showerror("Error", f"Error al actualizar la tabla: {error}")

    def limpiar_entries(self):
        for entry in self.entries.values():
            entry.delete(0, END)









