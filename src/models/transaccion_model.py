class Transaccion:
    def __init__(self, activo, cantidad_acciones, precio_compra):
        self.__activo = activo
        self.__cantidad_acciones = cantidad_acciones
        self.__precio_compra = precio_compra
        self.__precio_venta = None
        self.__rendimiento = None

    def comprar(self, cantidad, saldo_disponible):
        if saldo_disponible < cantidad * self.__precio_compra:
            return "No tienes saldo suficiente para realizar la compra."
        self.__cantidad_acciones += cantidad
        return f"Compraste {cantidad} acciones de {self.__activo} a {self.__precio_compra} por acción."

    def vender(self, cantidad, precio_venta, cantidad_acciones_disponibles):
        if cantidad > cantidad_acciones_disponibles:
            return "No tienes suficientes acciones para vender."
        self.__cantidad_acciones -= cantidad
        self.__precio_venta = precio_venta
        return f"Vendiste {cantidad} acciones de {self.__activo} a {self.__precio_venta} por acción."
 
    def get_activo(self):
        return self.__activo

    def get_cantidad_acciones(self):
        return self.__cantidad_acciones

    def get_precio_compra(self):
        return self.__precio_compra

    def get_precio_venta(self):
        return self.__precio_venta

    def get_rendimiento(self):
        return self.__rendimiento