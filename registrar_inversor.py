import mysql.connector
from util.validaciones import validar_cuit_o_cuil, validar_nombre_o_apellido, validar_email, validar_contrasena, validar_tipo_persona
from models.inversor_model import Invesor
from util.conexion_bd import obtener_conexion
from dao.inversor_dao import InversorDAO

def solicitar_dato(mensaje, validacion, mensaje_error):
    dato = input(mensaje)
    while not validacion(dato):
        print(mensaje_error)
        dato = input(mensaje)
    return dato

def registrar_inversor():
    print('---> REGISTRO <---')
    cuit_o_cuil = int(solicitar_dato('Ingresa el CUIT o CUIL: ', validar_cuit_o_cuil,
                                     'El dato ingresado es incorrecto, debe contener 11 dígitos sin espacios ni guiones.'))
    nombre = solicitar_dato('Ingresa el nombre: ', validar_nombre_o_apellido,
                            'El dato ingresado es incorrecto, debe contener solo letras.').lower()
    apellido = solicitar_dato('Ingresa el apellido: ', validar_nombre_o_apellido,
                              'El dato ingresado es incorrecto, debe contener solo letras.').lower()
    email = solicitar_dato('Ingrese el email: ', validar_email,
                           'El dato ingresado es incorrecto, inténtelo nuevamente.').lower()
    contrasena = solicitar_dato('Ingrese la contraseña, mínimo 8 caracteres, minúsculas, mayúsculas, números y caracteres especiales: ', validar_contrasena,
                                'La contraseña no cumple con los requisitos, inténtelo nuevamente.')
    tipo_persona = solicitar_dato('Ingrese tipo de persona física o jurídica (0/1): ', validar_tipo_persona,
                                  'El dato ingresado es incorrecto, debe ser 0 para física o 1 para jurídica.')
    
    inversor = Inversor(cuit_o_cuil, nombre, apellido, email, contrasena, int(tipo_persona), saldo_inicial=1000000)
    conexion = obtener_conexion()
    
    inversor_dao = InversorDAO(conexion)
    try:
        # Verificar si el tipo de inversor es 0 o 1
        if tipo_persona not in ('0', '1'):
            raise ValueError("El tipo de inversor debe ser 0 o 1")

        # Convertir tipo_inversor a entero
        tipo_persona = int(tipo_persona)

        # Obtener el id_tipo_inversor correspondiente
        result = inversor_dao.obtener_tipo_inversor(tipo_persona)
        if result:
            id_tipo_inversor = result[0]
        else:
            raise ValueError("El tipo de inversor no es válido")

        # Insertar inversor
        inversor_dao.insertar_inversor(id_tipo_inversor, cuit_o_cuil, nombre, apellido, email, contrasena, inversor.get_saldo_inicial())
        print("Inversor registrado con éxito:")
        print(inversor.mostrar_datos())
    except (mysql.connector.Error, ValueError) as err:
        print(f"Error: {err}")
        conexion.rollback()
    finally:
        conexion.close()

if __name__ == '__main__':
    registrar_inversor()