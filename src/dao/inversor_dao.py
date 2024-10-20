from datetime import date
from src.dao.interface_dao import DataAccessDAO

class InversorDAO(DataAccessDAO):
    def __init__(self, connection):
        self.connection = connection

    def obtener_tipo_inversor(self, tipo_inversor):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id_tipo_inversor FROM tipo_inversor WHERE id_tipo_inversor = %s", (tipo_inversor,))
        result = cursor.fetchone()
        cursor.close()
        return result

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
        cursor.execute("SELECT * FROM inversor WHERE email = %s", (email,))
        result = cursor.fetchone()
        cursor.close()
        return result

    # Implementaciones vacías de los métodos abstractos
    def obtener(self, email):
        pass

    def obtener_todos(self):
        pass

    def crear(self, objeto):
        pass

    def actualizar(self, objeto):
        pass

    def eliminar(self, id):
        pass