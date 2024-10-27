from src.dao.inversor_dao import InversorDAO
from src.util.conexion_bd import obtener_conexion
from src.util.validaciones import validar_email, validar_contrasena

def solicitar_dato(mensaje, validacion, mensaje_error):
    dato = input(mensaje)
    while not validacion(dato):
        print(mensaje_error)
        dato = input(mensaje)
    return dato

def iniciar_sesion():
    conexion = obtener_conexion()
    inversor_dao = InversorDAO(conexion)

    email = solicitar_dato('Ingrese su email: ', validar_email, 'El email ingresado no es válido.')
    contrasena = solicitar_dato('Ingrese su contraseña: ', validar_contrasena, 'La contraseña no es válida.')

    inversor = inversor_dao.obtener_inversor_por_email(email)
    if inversor:
        email_registrado = inversor.get_correo()  
        contrasena_registrada = inversor.get_contrasena() 
        if contrasena == contrasena_registrada:
            print(f"Inicio de sesión exitoso. Bienvenido, {inversor.get_nombre()}!")
            return True, inversor.get_correo(), inversor.get_cuit()
        else:
            print("Contraseña incorrecta.")
            return False, None, None
    else:
        print("Email no encontrado.")
        return False, None, None
