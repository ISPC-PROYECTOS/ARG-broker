#importar iniciar sesion,registrar inversor

def main():
    print('-----> MENÚ PRINCIPAL <-----')
    print('1. Iniciar Sesión.')
    print('2.Registrar nuevo inversor')
    print('3. Salir')
    salir=False
    
    while not salir:
        
        opcion = int(input('Ingrese la opción elegida: '))
        if opcion == 1:
            #iniciar_sesion() que va a llamar al modulo panel de control
            print("da opcion iniciar sesion")
        elif opcion == 2:
            #registar_inversor() 
            print("Da la opcion de regitrar nuevo inversor")
        elif opcion == 3:
            print("Gracias por usar nuestro programa.\
                  Saliendo de la aplicación.")
            salir = True
        else:
            print('Opción incorrecta, intente nuevamente.')


#prueba

if __name__ == '__main__':
    main()