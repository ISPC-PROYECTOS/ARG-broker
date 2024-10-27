import mysql.connector

class TransaccionDAO:
    def __init__(self, connection):
        self.connection = connection

    def verificar_saldo(self, cuit_o_cuil, cantidad, precio_compra):
        cursor = self.connection.cursor()
        try:
            query = """
                SELECT saldo_cuenta FROM inversor
                WHERE cuit_o_cuil = %s
            """
            cursor.execute(query, (cuit_o_cuil,))
            saldo = cursor.fetchone()[0]

            return saldo >= cantidad * precio_compra
        except mysql.connector.Error as error:
            raise error
        finally:
            cursor.close()

    def verificar_acciones(self, cuit_o_cuil, id_cotizacion_accion, cantidad):
        cursor = self.connection.cursor()
        try:
            query = """
                SELECT cantidad_acciones FROM portafolio
                WHERE cuit_o_cuil = %s AND id_cotizacion_accion = %s
            """
            cursor.execute(query, (cuit_o_cuil, id_cotizacion_accion))
            acciones_disponibles = cursor.fetchone()[0]

            return acciones_disponibles >= cantidad
        except mysql.connector.Error as error:
            raise error
        finally:
            cursor.close()

    def guardar_transaccion(self, tipo_transaccion, cuit_inversor, id_cotizacion, cantidad_acciones, valor_transaccion):
        with self.conexion.cursor() as cursor:
            query = """
            INSERT INTO transaccion (id_tipo_transaccion, cuit_o_cuil, id_cotizacion_accion, cantidad_acciones_transaccion, fecha_hora_transaccion, valor_transaccion, )
            VALUES (%s, %s, %s, %s, NOW(), %s)
            """
            cursor.execute(query, (tipo_transaccion, cuit_inversor, id_cotizacion, cantidad_acciones, valor_transaccion))
            self.conexion.commit()