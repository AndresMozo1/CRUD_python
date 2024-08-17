from Conexion import *

class CProductos:

    @staticmethod
    def mostrarProductos():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("SELECT * FROM productos;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error al mostrar productos: {}".format(error))

    @staticmethod
    def ingresarProductos(nombre, precio, cantidad):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "INSERT INTO productos VALUES (NULL, %s, %s, %s);"
            valores = (nombre, precio, cantidad)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Producto ingresado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error al ingresar producto: {}".format(error))

    @staticmethod
    def modificarProducto(idProducto, nombre, precio, cantidad):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE productos SET nombre = %s, precio = %s, cantidad = %s WHERE id = %s;"
            valores = (nombre, precio, cantidad, idProducto)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Producto actualizado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error al actualizar producto: {}".format(error))

    @staticmethod
    def eliminarProducto(idProducto):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE FROM productos WHERE id = %s;"
            valores = (idProducto,)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Producto eliminado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error al eliminar producto: {}".format(error))
