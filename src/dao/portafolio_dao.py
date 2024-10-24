from src.dao.interface_dao import DataAccessDAO
from src.models.portafolio_model import Portafolio
import mysql.connector

class PortafolioDAO(DataAccessDAO):
    def __init__(self, connection):
        self.connection = connection

    def obtener_transacciones(self, cuit_o_cuil):
        cursor = self.connection.cursor()
        try:
            query = """
                SELECT id_num_transaccion, id_tipo_transaccion, cuit_o_cuil, 
                    id_cotizacion_accion, cantidad_acciones_transaccion, 
                    fecha_hora_transaccion, valor_transaccion 
                FROM transaccion 
                WHERE cuit_o_cuil = %s
            """
            cursor.execute(query, (cuit_o_cuil,))
            rows = cursor.fetchall()
            
            transacciones = []
            for row in rows:
                transacciones.append({
                    'id_num_transaccion': row[0],
                    'id_tipo_transaccion': row[1],
                    'cuit_o_cuil': row[2],
                    'id_cotizacion_accion': row[3],
                    'cantidad_acciones_transaccion': row[4],
                    'fecha_hora_transaccion': row[5],
                    'valor_transaccion': row[6]
                })
            
            if transacciones:
                portafolio = Portafolio()
                portafolio.mostrar_transacciones(transacciones)
                return portafolio
            return None
        except mysql.connector.Error as error:
            raise error
        finally:
            cursor.close()

    
    def obtener_suma_transacciones(self, cuit_o_cuil):
        cursor = self.connection.cursor()
        try:
            query = """
                SELECT SUM(valor_transaccion) 
                FROM transaccion 
                WHERE cuit_o_cuil = %s
            """
            cursor.execute(query, (cuit_o_cuil,))
            row = cursor.fetchone()
            suma_transacciones = row[0] if row and row[0] is not None else 0
            
            portafolio = Portafolio()
            saldo_total = portafolio.calcular_saldo_cuenta(suma_transacciones)
            portafolio.mostrar_saldo_cuenta()
            
            return saldo_total
        except mysql.connector.Error as error:
            raise error
        finally:
            cursor.close()

    def calcular_rendimiento_total(self, cuit_o_cuil):
        cursor = self.connection.cursor()
        try:
            query = """
                SELECT t.id_cotizacion_accion, t.cantidad_acciones_transaccion, 
                       t.valor_transaccion, t.tipo_transaccion, c.precio_actual
                FROM brokercba.transaccion t
                INNER JOIN brokercba.cotizacion c ON t.id_cotizacion_accion = c.id_cotizacion_accion
                WHERE t.cuit_o_cuil = %s
            """
            cursor.execute(query, (cuit_o_cuil,))
            transacciones_con_precios = cursor.fetchall()

            transacciones = []
            for row in transacciones_con_precios:
                transacciones.append({
                    'id_cotizacion_accion': row[0],
                    'cantidad_acciones_transaccion': row[1],
                    'valor_transaccion': row[2],
                    'tipo_transaccion': row[3],
                    'precio_actual': row[4]
                })

            portafolio = Portafolio()
            rendimiento_total = portafolio.calcular_rendimiento(transacciones)
            print(f"Rendimiento total del portafolio: {rendimiento_total}")
            return rendimiento_total
        except mysql.connector.Error as error:
            raise error
        finally:
            cursor.close()

