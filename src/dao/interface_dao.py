from abc import ABC, abstractmethod

class DataAccessDAO(ABC):
    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def crear(self, objeto):
        pass

    @abstractmethod
    def actualizar(self, objeto):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass

    @abstractmethod
    def obtener_tipo_inversor(self, tipo_inversor):
        pass

    @abstractmethod
    def insertar_inversor(self, id_tipo_inversor, cuit_o_cuil, nombre, apellido, email, contrasena, saldo_inicial):
        pass

    @abstractmethod
    def obtener_inversor_por_email(self, email):
        pass

    @abstractmethod
    def obtener_transacciones(self, cuit_o_cuil):
        pass

    @abstractmethod
    def obtener_suma_transacciones(self, cuit_o_cuil):
        pass

    @abstractmethod
    def calcular_rendimiento_total(self, cuit_o_cuil):
        pass

    @abstractmethod
    def obtener_cotizaciones(self):
        pass