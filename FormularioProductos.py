from formulario_base import FormularioBase
from Productos import CProductos

class FormularioProductos(FormularioBase):
    def __init__(self):
        super().__init__(
            title="Formulario Productos",
            bg_color="#004080",
            campos=["Id", "Nombre", "Precio", "Cantidad"],
            obtener_datos=CProductos.mostrarProductos,
            insertar_datos=CProductos.ingresarProductos,
            modificar_datos=CProductos.modificarProducto,
            eliminar_datos=CProductos.eliminarProducto
        )
        self.base.grab_set()

    def agregar_boton_cerrar(self):
        btn_cerrar = Button(self.base, text="Cerrar", command=self.cerrar, bg="#F2E8C6")
        btn_cerrar.grid(row=len(self.campos)+1, column=0, pady=10)