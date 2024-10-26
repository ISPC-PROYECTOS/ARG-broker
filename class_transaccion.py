from src.dao.transaccion_dao import TransaccionDAO

class Transaccion:
    def __init__(self, activo, cantidad_acciones, precio_compra, connection):
        self.__activo = activo
        self.__cantidad_acciones = cantidad_acciones
        self.__precio_compra = precio_compra
        self.__precio_venta = None
        self.__rendimiento = None
        self.connection = connection  # Conexión a la base de datos
        self.transaccion_dao = TransaccionDAO(self.connection)  # DAO para la transacción


    def comprar(self, usuario_id, cantidad, precio):
        # Verificamos si el usuario tiene suficiente saldo para realizar la compra
        if self.transaccion_dao.verificar_saldo(usuario_id, cantidad * precio):
            # Si tiene suficiente saldo, se realiza la compra
            self.__cantidad_acciones += cantidad
            self.__precio_compra = precio
            
            # Se registra la transacción en la base de datos
            self.transaccion_dao.insertar_transaccion(self)
            
            # Retornamos el mensaje de confirmación
            return f"Compra exitosa: {cantidad} acciones de {self.__activo} a {precio} por acción."
        else:
            return "No tienes suficiente saldo para realizar esta compra."

       
    def vender(self, usuario_id, cantidad, precio):
        # Verificamos si el usuario tiene suficientes acciones para vender
        if self.transaccion_dao.verificar_acciones(usuario_id, self.__activo, cantidad):
            # Si tiene suficientes acciones, se realiza la venta
            self.__cantidad_acciones -= cantidad
            self.__precio_venta = precio
            
        
            # Retornamos el mensaje de confirmación 
            return f"Venta exitosa: {cantidad} acciones de {self.__activo} a {precio} por acción."
        else:
            return "No tienes suficientes acciones para vender."


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
