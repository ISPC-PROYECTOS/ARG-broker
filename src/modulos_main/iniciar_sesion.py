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
        email_registrado, contrasena_registrada = inversor[4], inversor[5]
        if contrasena == contrasena_registrada:
            print(f"Inicio de sesión exitoso. Bienvenido, {email_registrado}!")
            return True
        else:
            print("Contraseña incorrecta.")
            return False
    else:
        print("Email no encontrado.")
        return False

if __name__ == '__main__':
    iniciar_sesion()