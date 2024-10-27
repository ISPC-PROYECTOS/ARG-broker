from src.dao.portafolio_dao import PortafolioDAO
from src.util.conexion_bd import obtener_conexion
from src.dao.inversor_dao import InversorDAO

def panel_de_control(email_inversor, cuit_inversor):
    salir = False

    while not salir: 
        print('-----> PANEL DE CONTROL <-----')
        print("1. Ver mi Saldo.")
        print("2. Historial de transacciones y sus rendimientos.")
        print("3. Comprar.")
        print("4. Vender.")
        print("5. Cerrar sesión.")  

        opcion_panel = int(input("Ingrese la opción elegida: "))
        
        # Abre la conexión a la base de datos
        conexion = obtener_conexion()
        
        if opcion_panel == 1:
            portafolio_dao = PortafolioDAO(conexion)
            saldo = portafolio_dao.obtener_suma_transacciones(cuit_inversor)  # Usa email_inversor directamente
            print(f"Saldo total: {saldo}")    

        elif opcion_panel == 2:
            # Aquí deberías llamar a la función que muestra el historial de transacciones
            print("Mostrando historial de transacciones")

        elif opcion_panel == 3: 
            # Lógica para comprar
            print("Comprar acciones")

        elif opcion_panel == 4: 
            # Lógica para vender
            print("Vender acciones")
            
        elif opcion_panel == 5: 
            print("Sesión cerrada. Volviendo al menú anterior")
            salir = True  # Salir del panel de control
        else: 
            print("Opción ingresada inválida, intentá nuevamente.")