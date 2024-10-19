from abc import ABC, abstractmethod

class DataAccessDAO(ABC):
    @abstractmethod
    def obtener(self,cuit_o_cuil):
        pass

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