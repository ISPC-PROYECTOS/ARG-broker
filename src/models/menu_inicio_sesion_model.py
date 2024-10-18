from main import main

def panel_de_control():
    print("Bienvenido al panel de Control, elija una opcion por favor")
    print("1- Mostrar saldo actual.")
    print("2- Historial de transacciones.")
    print("3- Rendimiento de inverciones.")
    print("4- Comprar.")
    print("5- Vender.")   
    print("6- Cerrar sesion.")  

    salir=False

    while not salir: 
        opcion_panel= int(input("Ingrese su opcion: "))
        if opcion_panel==1:
            #llamar funcion mostrar saldo
            print ("mostrar saldo")
        elif opcion_panel==2:
            #llamar funcion mostrar historial de transacciones
            print("mostrando historial de transacciones")
        elif opcion_panel ==3: 
            #llamar funcion mostrar rendimiento de invercion
            print("Mostrar rendimiento de inverciones")
        elif opcion_panel ==4: 
            #Comprar
            print("Comprar acciones")
        elif opcion_panel ==5: 
            #Vender
            print("Vender acciones")
        elif opcion_panel ==6: 
            #llamar cerrar sesion
            #volver al menu principal
            print("Sesion cerrada. Volviendo al menu anterior")
            main()
            salir=True
        else: 
            print("opcion ingresada invalida, intenta nuevamente.")
"""
#probando
if __name__== "__main__":
    panel_de_control()"""