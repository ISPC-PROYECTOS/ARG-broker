class Portafolio():
    def __init__(self, estado=True, saldo_inicial=1000000,rendimiento=None):
        self.__estado = estado
        self.__saldo_inicial = saldo_inicial
        self.__saldo_cuenta = saldo_inicial
        self.__transacciones = []
        self.__rendimiento= rendimiento

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
    
    def get__rendimiento(self):
        return self.__rendimiento

    def set__rendimiento(self,rendimiento):
        self.__rendimiento=rendimiento

    def calcular_saldo_cuenta(self, suma_transacciones):
        self.__saldo_cuenta = self.__saldo_inicial + suma_transacciones
        return self.__saldo_cuenta
        
    def mostrar_saldo_cuenta(self):
        
        return f"Saldo de la cuenta: {self.__saldo_cuenta}"

    def mostrar_transacciones(self):
        
        return f"Transacciones: {self.__transacciones}"

    def calcular_rendimiento(self, transacciones_con_precios):
        rendimiento_total = 0
        for transaccion in transacciones_con_precios:
            cantidad_acciones = transaccion['cantidad_acciones_transaccion']
            valor_transaccion = transaccion['valor_transaccion']
            precio_actual = transaccion['precio_actual']
            tipo_transaccion = transaccion['tipo_transaccion']

            if tipo_transaccion == "compra":
                rendimiento_accion = (precio_actual - valor_transaccion) * cantidad_acciones
            elif tipo_transaccion == "venta":
                rendimiento_accion = (valor_transaccion - precio_actual) * cantidad_acciones

            rendimiento_total += rendimiento_accion

        return rendimiento_total
    
    def mostrar_rendieminto(self):
        return f"Su rendimiento actual es: {self.__rendimiento}"
        
