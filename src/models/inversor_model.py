class Inversor:
    def __init__(self, cuit_o_cuil, nombre, apellido, email, contrasena, tipo_de_persona, saldo_inicial=1000000):
        self.__cuit_o_cuil = cuit_o_cuil
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasena = contrasena
        self.__tipo_de_persona = tipo_de_persona
        self.__saldo_inicial = saldo_inicial

    def get_cuit(self):
        return self.__cuit_o_cuil

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_correo(self):
        return self.__email

    def get_tipo_de_persona(self):
        return self.__tipo_de_persona
    
    def get_contrasena (self):
        return self.__contrasena
    
    def get_saldo_inicial(self):
        return self.__saldo_inicial
    
    #No muestra la contrasena por seguridad
    def mostrar_datos(self):
        return (f"CUIT: {self.__cuit_o_cuil}\n"
                f"Nombre: {self.__nombre}\n"
                f"Apellido: {self.__apellido}\n"
                f"Email: {self.__email}\n"
                f"Tipo de Persona: {self.__tipo_de_persona}\n"
                f"Saldo Inicial: {self.__saldo_inicial}")