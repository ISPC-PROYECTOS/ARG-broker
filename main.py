from src.modulos_main.iniciar_sesion import iniciar_sesion
from src.modulos_main.registrar_inversor import registrar_inversor

def main():
    print('-----> MENÚ PRINCIPAL <-----')
    print('1. Iniciar Sesión.')
    print('2.Registrar nuevo inversor')
    print('3. Salir')
    salir=False
    
    while not salir:
        
        opcion = int(input('Ingrese la opción elegida: '))
        if opcion == 1:
            iniciar_sesion()            
        elif opcion == 2:
            registrar_inversor()
            pass
        elif opcion == 3:
            print("Gracias por usar nuestro programa.\
                  Saliendo de la aplicación.")
            salir = True
        else:
            print('Opción incorrecta, intente nuevamente.')


#prueba

if __name__ == '__main__':
    main()