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

    def calcular_saldo_cuenta(self, suma_transacciones):
        self.__saldo_cuenta = self.__saldo_inicial + suma_transacciones
        return self.__saldo_cuenta        

    def mostrar_saldo_cuenta(self):
        return f"Saldo de la cuenta: {self.__saldo_cuenta}"

    def mostrar_transacciones(self, transacciones):
        return [
            (f"ID Transacción: {transaccion['id_num_transaccion']}, "
             f"Tipo: {transaccion['id_tipo_transaccion']}, "
             f"Acción: {transaccion['id_cotizacion_accion']}, "
             f"Cantidad: {transaccion['cantidad_acciones_transaccion']}, "
             f"Valor: {transaccion['valor_transaccion']}, "
             f"Fecha: {transaccion['fecha_hora_transaccion']}")
            for transaccion in transacciones
        ]
        
    def mostrar_total_invertido(self, suma_transacciones):
        return f" Su total invertido es: {suma_transacciones} "

    def calcular_rendimiento(self, transacciones):
        rendimiento_total = 0
        inversion_inicial_total = 0

        for transaccion in transacciones:
            cantidad_acciones = transaccion['cantidad_acciones_transaccion']
            precio_venta = transaccion['precio_venta']
            precio_compra = transaccion['precio_compra']
            
            inversion_inicial_total += precio_compra * cantidad_acciones
            
            rendimiento_accion = (precio_venta - precio_compra) * cantidad_acciones
            rendimiento_total += rendimiento_accion

        rendimiento_porcentual = (rendimiento_total / inversion_inicial_total) * 100 if inversion_inicial_total > 0 else 0
        return round(rendimiento_total, 2), round(rendimiento_porcentual, 2)
    
    def mostrar_rendimiento(self, rendimiento_total, rendimiento_porcentual):
        return (f"Rendimiento total: {round(rendimiento_total, 2)}\n"
                f"Rendimiento porcentual: {round(rendimiento_porcentual, 2)}%")