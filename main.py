from src.modulos_main import iniciar_sesion, registrar_inversor, panel_de_control

def main():
    salir = False
    
    while not salir:
        print('-----> MENÚ PRINCIPAL <-----')
        print('1. Iniciar Sesión.')
        print('2. Registrar nuevo inversor.')
        print('3. Salir.')
        opcion = int(input('Ingrese la opción elegida: '))
        if opcion == 1:
            if iniciar_sesion.iniciar_sesion() == True:
                panel_de_control.panel_de_control()
        if opcion == 2:
            registrar_inversor.registrar_inversor()
        if opcion == 3:
            salir = True
            print("Gracias por usar nuestro programa.\nSaliendo de la aplicación.")
        else:
            print('Opción incorrecta, intente nuevamente.')


if __name__ == '__main__':
    main()