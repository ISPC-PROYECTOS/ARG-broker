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
            
            return transacciones if transacciones else None
        except mysql.connector.Error as error:
            raise error
        finally:
            cursor.close()

    def obtener_suma_transacciones(self, cuit_o_cuil):
        cursor = self.connection.cursor()
        try:
            query = """
                SELECT id_tipo_transaccion, valor_transaccion 
                FROM transaccion 
                WHERE cuit_o_cuil = %s
            """
            cursor.execute(query, (cuit_o_cuil,))
            rows = cursor.fetchall()

            suma_transacciones = 0
            for row in rows:
                tipo_transaccion = row[0]
                valor_transaccion = row[1]
                
                if tipo_transaccion == 1:  
                    suma_transacciones -= valor_transaccion  
                elif tipo_transaccion == 2:  
                    suma_transacciones += valor_transaccion  

            portafolio = Portafolio(saldo_inicial=1000000)
            saldo_total = portafolio.calcular_saldo_cuenta(suma_transacciones)
            return saldo_total
        except mysql.connector.Error as error:
            raise error
        finally:
            cursor.close()

    def calcular_rendimiento(self, cuit_o_cuil):
        cursor = self.connection.cursor()
        try:
            query = """
                SELECT t.id_cotizacion_accion, t.cantidad_acciones_transaccion,
                    t.valor_transaccion, c.precio_venta, c.precio_compra
                FROM brokercba.transaccion t
                INNER JOIN brokercba.cotizacion c ON t.id_cotizacion_accion = c.id_cotizacion_accion
                WHERE t.cuit_o_cuil = %s
            """
            cursor.execute(query, (cuit_o_cuil,))
            transacciones_con_precios = cursor.fetchall()

            transacciones = [
                {
                    'id_cotizacion_accion': row[0],
                    'cantidad_acciones_transaccion': row[1],
                    'valor_transaccion': row[2],
                    'precio_venta': row[3],
                    'precio_compra': row[4]
                }
                for row in transacciones_con_precios
            ]

            portafolio = Portafolio(cuit_o_cuil)
            rendimiento_total, rendimiento_porcentual = portafolio.calcular_rendimiento(transacciones)
            print(f"Rendimiento total del portafolio: {rendimiento_total:.2f}")
            print(f"Rendimiento porcentual del portafolio: {rendimiento_porcentual:.2f}%")           
            return rendimiento_total, rendimiento_porcentual
        except mysql.connector.Error as error:
            raise error
        finally:
            cursor.close()

    def registrar_transaccion(self, cuit_inversor, simbolo, cantidad, precio_compra):
        cursor = self.connection.cursor()
        try:
            query_accion = "SELECT id_accion FROM brokercba.accion WHERE simbolo_accion = %s"
            cursor.execute(query_accion, (simbolo,))
            id_accion = cursor.fetchone()

            if not id_accion:
                print("No se encontró la acción con el símbolo proporcionado.")
                return

            id_accion = id_accion[0]
            
            query_transaccion = """
                INSERT INTO brokercba.transaccion (cuit_o_cuil, id_cotizacion_accion, cantidad_acciones_transaccion, valor_transaccion, id_tipo_transaccion)
                VALUES (%s, %s, %s, %s, %s)
            """
            id_tipo_transaccion = 1 
            valor_transaccion = cantidad * precio_compra  
            cursor.execute(query_transaccion, (cuit_inversor, id_accion, cantidad, valor_transaccion, id_tipo_transaccion))

            self.connection.commit()
            print(f"Transacción de compra registrada con éxito para {cantidad} acciones de {simbolo}.")
        except mysql.connector.Error as error:
            print(f"Error al registrar la transacción: {error}")
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

    def obtener_cotizaciones(self):
        pass

    def actualizar_cantidad_disponible(self, id_cotizacion, cantidad_a_restar):
        pass