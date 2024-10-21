class Portafolio():
    def __init__(self, estado=True, saldo_inicial=1000000,rendimiento=None):
        self.__estado = estado
        self.__saldo_inicial = saldo_inicial
        self.__saldo_cuenta = saldo_inicial
        self.__transacciones = []
        self.__rendimiento= rendimiento if rendimiento is not None else 0

    def get_estado(self):
        return self.__estado
    
    def set_estado(self, estado):
        self.__estado = estado

    def get_saldo_inicial(self):
        return self.__saldo_inicial

    def get_saldo_cuenta(self):
        return self.__saldo_cuenta
    
    def set_saldo_cuenta(self, saldo_cuenta):
        self.__saldo_cuenta = saldo_cuenta
    
    def set_transacciones(self, transacciones):
        self.__transacciones = transacciones

    def get_transacciones(self):
        return self.__transacciones
    
    def get_rendimiento(self):
        return self.__rendimiento

    def set_rendimiento(self,rendimiento):
        self.__rendimiento=rendimiento

    def mostrar_saldo_cuenta(self):
        return f"Saldo de la cuenta: {self.__saldo_cuenta}"

    def mostrar_transacciones(self):
        return f"Transacciones: {self.__transacciones}"

    def calcular_rendimiento(self, suma_precio_venta, suma_precio_compra):
        rendimiento = suma_precio_venta - suma_precio_compra
        return self.__rendimiento
    
    def mostrar_rendimiento(self):
        return f"Su rendimiento actual es: {self.__rendimiento}"