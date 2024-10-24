class Transaccion:
    def __init__(self, activo, cantidad_acciones, precio_compra):
        self.__activo = activo
        self.__cantidad_acciones = cantidad_acciones
        self.__precio_compra = precio_compra
        self.__precio_venta = None
        self.__rendimiento = None

    def comprar(self, cantidad, precio):
        self.__cantidad_acciones += cantidad
        self.__precio_compra = precio
        print(f"Compraste {cantidad} acciones de {self.__activo} a {precio} por acción.")
    def vender(self, cantidad, precio):
        if cantidad > self.__cantidad_acciones:
            print("No tienes suficientes acciones para vender.")
        else:
            self.__cantidad_acciones -= cantidad
            self.__precio_venta = precio
            print(f"Vendiste {cantidad} acciones de {self.__activo} a {precio} por acción.")
            self.calcular_rendimiento()

    def calcular_rendimiento(self):
        if self.__precio_venta is not None:
            self.__rendimiento = (self.__precio_venta - self.__precio_compra) * self.__cantidad_acciones
            print(f"El rendimiento de la transacción es: {self.__rendimiento}")
        else:
            print("Aún no has vendido las acciones.")

    def obtener_activo(self):
        return self.__activo

    def obtener_cantidad_acciones(self):
        return self.__cantidad_acciones

    def obtener_precio_compra(self):
        return self.__precio_compra

    def obtener_precio_venta(self):
        return self.__precio_venta

    def obtener_rendimiento(self):
        return self.__rendimiento
