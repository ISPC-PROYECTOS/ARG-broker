from inversor_dao import InversorDAO
from conexion_bd import obtener_conexion
from validaciones import validar_email, validar_contrasena
from registrar_inversor import solicitar_dato

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