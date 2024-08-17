from formulario_base import FormularioBase
from Clientes import CClientes

class FormularioClientes(FormularioBase):
    def __init__(self):
        super().__init__(
            title="Formulario Clientes",
            bg_color="#800000",
            campos=["Id", "Nombres", "Apellidos", "Sexo"],
            obtener_datos=CClientes.mostrarClientes,
            insertar_datos=CClientes.ingresarClientes,
            modificar_datos=CClientes.modificarClientes,
            eliminar_datos=CClientes.EliminarClientes
        )
        self.base.grab_set()

    
    def agregar_boton_cerrar(self):
        btn_cerrar = Button(self.base, text="Cerrar", command=self.cerrar, bg="#F2E8C6")
        btn_cerrar.grid(row=len(self.campos)+1, column=0, pady=10)    