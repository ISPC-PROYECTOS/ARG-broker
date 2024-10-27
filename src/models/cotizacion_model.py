import datetime
class Cotizacion:
    def __init__(self, nombre, simbolo, fecha_hora, precio_venta, precio_compra, cantidad_disponible):
        self.__nombre = nombre
        self.__simbolo = simbolo
        if isinstance(fecha_hora, str):
            self.__fecha_hora = datetime.strptime(fecha_hora, '%Y-%m-%d %H:%M:%S')
        else:
            self.__fecha_hora = fecha_hora        
        self.__precio_venta = precio_venta
        self.__precio_compra = precio_compra
        self.__cantidad_disponible = cantidad_disponible

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_simbolo(self):
        return self.__simbolo

    def set_simbolo(self, simbolo):
        self.__simbolo = simbolo

    def get_fecha_hora(self):
        return self.__fecha_hora.strftime('%Y-%m-%d %H:%M:%S')
    
    def set_fecha_hora(self, fecha_hora):
        self.__fecha_hora = fecha_hora

    def get_precio_venta(self):
        return self.__precio_venta

    def set_precio_venta(self, precio_venta):
        self.__precio_venta = precio_venta

    def get_precio_compra(self):
        return self.__precio_compra

    def set_precio_compra(self, precio_compra):
        self.__precio_compra = precio_compra

    def get_cantidad_disponible(self):
        return self.__cantidad_disponible

    def set_cantidad_disponible(self, cantidad_disponible):
        self.__cantidad_disponible = cantidad_disponible

    def maximo_dia(self):
        pass

    def minimo_dia(self):
        pass

    def ultimo_operado(self):
        pass

    def ultimo_cierre(self):
        pass

    def mostrar_cotizacion(self):
        return f"Nombre: {self.get_cotizacion()}, Símbolo: {self.get_simbolo()}, Fecha y Hora: {self.get_fecha_hora()}, Precio Venta: {self.get_precio_venta()}, Precio Compra: {self.get_precio_compra()}, Cantidad Disponible: {self.get_cantidad_disponible()}"