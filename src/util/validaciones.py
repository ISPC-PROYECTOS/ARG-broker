import re

def validar_cuit_o_cuil(cuit_o_cuil):
    if cuit_o_cuil.isdigit() and (len(cuit_o_cuil) == 11):
        return True
    return False

def validar_nombre_o_apellido(nombre_o_apellido):
    nombre_o_apellido = nombre_o_apellido
    if nombre_o_apellido.isalpha():
        return True
    return False

def validar_email(email):
    email = email
    if '@' in email and '.com' in email:
        return True
    return False 

def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False
    if not re.search(r"[a-z]", contrasena):
        return False
    if not re.search(r"[A-Z]", contrasena):
        return False
    if not re.search(r"[0-9]", contrasena):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasena):
        return False
    return True

def validar_tipo_persona(tipo_persona):
    if tipo_persona.isdigit() and tipo_persona == '0':
        return True
    if tipo_persona.isdigit() and tipo_persona == '1':
        return True
    return False