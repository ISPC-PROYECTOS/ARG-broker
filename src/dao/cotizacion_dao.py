from src.dao.interface_dao import DataAccessDAO
from src.models.cotizacion_model import Cotizacion
import mysql.connector
from src.util.conexion_bd import obtener_conexion

class CotizacionDAO(DataAccessDAO):
    def __init__(self, connection):
        self.connection = connection

    def obtener_cotizaciones(self):
        cursor = self.connection.cursor()
        try:
            query = (
                "SELECT "
                "a.nombre_accion, "
                "a.simbolo_accion, "
                "c.fecha_hora, "
                "c.precio_venta, "
                "c.precio_compra "
                "FROM "
                "cotizacion c "
                "JOIN "
                "accion a ON c.id_accion = a.id_accion;"
            )
            cursor.execute(query)
            rows = cursor.fetchall()
            
            cotizaciones = []
            for row in rows:
                cotizacion = Cotizacion(row[0], row[1], row[2], row[3], row[4])
                cotizaciones.append(cotizacion)
            return cotizaciones
        except mysql.connector.Error as error:
            raise error
        finally:
            cursor.close()

    def obtener_todos(self):
        pass

    def crear(self, objeto):
        pass

    def actualizar(self, objeto):
        pass

    def eliminar(self, id):
        pass

    def obtener_tipo_inversor(self, tipo_inversor):
        pass

    def insertar_inversor(self, id_tipo_inversor, cuit_o_cuil, nombre, apellido, email, contrasena, saldo_inicial):
        pass

    def obtener_inversor_por_email(self, email):
        pass

    def obtener_transacciones(self, cuit_o_cuil):
        pass

    def obtener_suma_transacciones(self, cuit_o_cuil):
        pass

    def calcular_rendimiento_total(self, cuit_o_cuil):
        pass

if __name__ == '__main__':
    connection = obtener_conexion()

    try:
        cotizacion_dao = CotizacionDAO(connection)

        cotizaciones = cotizacion_dao.obtener_cotizaciones()

        print(f"{'Nombre':<35} {'Símbolo':<10} {'Fecha y Hora':<22} {'Precio Venta':<15} {'Precio Compra':<15}")
        print("=" * 100)

        for cotizacion in cotizaciones:
            print(f"{cotizacion.get_nombre():<35} {cotizacion.get_simbolo():<10} {cotizacion.get_fecha_hora():<22} {cotizacion.get_precio_venta():<15} {cotizacion.get_precio_compra():<15}")
    finally:
        connection.close()