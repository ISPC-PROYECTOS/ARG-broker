from main import main

def panel_de_control():
    print("Bienvenido al panel de Control, elija una opción por favor")
    print("1- Ver mi Saldo.")
    print("2- Historial de transacciones y sus rendimientos.")
    print("3- Comprar.")
    print("4- Vender.")   
    print("5- Cerrar sesión.")  

    salir=False

    #todos los print se borran cuando esten llamadas las funciones/metodos

    #todos los print se borran cuando esten llamadas las funciones/metodos

    while not salir: 
        #traer datos de inversor
        opcion_panel= int(input("Ingrese su opción: "))
        if opcion_panel==1:
            #llamar funcion mostrar saldo/total invertidos/rendimiento total
            print ("mostrar saldo/total invertido/rendieminto total")

        elif opcion_panel==2:
            #llamar funcion mostrar historial de transacciones y cotizacion actual compra y venta,mostrando el rendimiento actual
            print("mostrando historial de transacciones")

        elif opcion_panel ==3: 
            #Comprar
            print("Comprar acciones")

        elif opcion_panel ==4: 
            #Vender
            print("Vender acciones")
            
        elif opcion_panel ==5: 
            #llamar cerrar sesion
            #volver al menu principal
            print("Sesión cerrada. Volviendo al menu anterior")
            main()
            salir=True
        else: 
            print("Opción ingresada invalida, intentá nuevamente.")
"""
#probando
if __name__== "__main__":
    panel_de_control()"""