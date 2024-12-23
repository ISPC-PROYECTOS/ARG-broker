from datetime import date
from src.dao.interface_dao import DataAccessDAO
from src.models.inversor_model import Inversor
from src.util.conexion_bd import obtener_conexion

class InversorDAO(DataAccessDAO):
    def __init__(self, connection):
        self.connection = connection

    def obtener_tipo_inversor(self, tipo_inversor):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id_tipo_inversor FROM tipo_inversor WHERE id_tipo_inversor = %s", (tipo_inversor,))
        resultado = cursor.fetchone()
        cursor.close()
        return resultado

    def insertar_inversor(self, id_tipo_inversor, cuit_o_cuil, nombre, apellido, email, contrasena, saldo_inicial):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO inversor (id_tipo_inversor, cuit_o_cuil, nombre, apellido, email, contrasena, fecha_alta_inversor, saldo_inicial)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (id_tipo_inversor, cuit_o_cuil, nombre, apellido, email, contrasena, date.today(), saldo_inicial))
        self.connection.commit()
        cursor.close()
    
    def obtener_inversor_por_email(self, email):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT id_tipo_inversor, cuit_o_cuil, nombre, apellido, email, contrasena, saldo_inicial
            FROM inversor
            WHERE email = %s
        """, (email,))        
        resultado = cursor.fetchone()
        cursor.close()
        
        if resultado:
            inversor = Inversor(*resultado)
            return inversor
        return None
    
    def obtener_todos(self):
        pass

    def crear(self, objeto):
        pass

    def actualizar(self, objeto):
        pass

    def eliminar(self, id):
        pass

    def obtener_transacciones(self, cuit_o_cuil):
        pass

    def obtener_suma_transacciones(self, cuit_o_cuil):
        pass

    def calcular_rendimiento(self, cuit_o_cuil):
        pass

    def obtener_cotizaciones(self):
        pass

    def actualizar_cantidad_disponible(self, id_cotizacion, cantidad_a_restar):
        pass

    def registrar_transaccion(self, cuit_inversor, simbolo, cantidad, precio_compra):
        pass