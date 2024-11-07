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
                "c.precio_compra, "
                "c.cantidad_disponible "
                "FROM "
                "cotizacion c "
                "JOIN "
                "accion a ON c.id_accion = a.id_accion;"
            )
            cursor.execute(query)
            rows = cursor.fetchall()
            
            cotizaciones = []
            for row in rows:
                cotizacion = Cotizacion(row[0], row[1], row[2], row[3], row[4], row[5])
                cotizaciones.append(cotizacion)
            return cotizaciones
        except mysql.connector.Error as error:
            raise error
        finally:
            cursor.close()

    def actualizar_cantidad_disponible(self, simbolo, cantidad):
        cursor = self.connection.cursor()
        try:
            query = """
                UPDATE brokercba.cotizacion c
                JOIN brokercba.accion a ON c.id_accion = a.id_accion
                SET c.cantidad_disponible = c.cantidad_disponible + %s
                WHERE a.simbolo_accion = %s
            """
            cursor.execute(query, (cantidad, simbolo))
            self.connection.commit()
        except mysql.connector.Error as error:
            print(f"Error al actualizar cantidad disponible: {error}")
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

    def calcular_rendimiento(self, cuit_o_cuil):
        pass

    def registrar_transaccion(self, cuit_inversor, simbolo, cantidad, precio_compra):
        pass