from src.dao.portafolio_dao import PortafolioDAO
from src.util.conexion_bd import obtener_conexion

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
        
        conexion = obtener_conexion()
        
        if opcion_panel == 1:
            portafolio_dao = PortafolioDAO(conexion)
            saldo = portafolio_dao.obtener_suma_transacciones(cuit_inversor)
            print(f"Saldo total: {saldo:.2f}")    

        elif opcion_panel == 2:
            portafolio_dao = PortafolioDAO(conexion)
            transacciones = portafolio_dao.obtener_transacciones(cuit_inversor)

            if transacciones:
                print("\n---- Historial de Transacciones ----")
                print(f"{'ID':<10} {'Tipo':<10} {'CUIT/CUIL':<15} {'Acción':<15} {'Cantidad':<10} {'Fecha':<20} {'Valor':<10}")
                print("-" * 90)

                for transaccion in transacciones:
                    id_transaccion = transaccion['id_num_transaccion']
                    tipo_transaccion = "Compra" if transaccion['id_tipo_transaccion'] == 1 else "Venta"
                    cuit_o_cuil = transaccion['cuit_o_cuil']
                    id_cotizacion = transaccion['id_cotizacion_accion']
                    cantidad = transaccion['cantidad_acciones_transaccion']
                    fecha = transaccion['fecha_hora_transaccion'].strftime('%Y-%m-%d %H:%M')
                    valor = transaccion['valor_transaccion']

                    print(f"{id_transaccion:<10} {tipo_transaccion:<10} {cuit_o_cuil:<15} {id_cotizacion:<15} {cantidad:<10} {fecha:<20} {valor:<10}")

                print("-" * 90)
            else:
                print("No hay transacciones para mostrar.")

        elif opcion_panel == 3: 
            pass

        elif opcion_panel == 4: 
            # Lógica para vender
            print("Vender acciones")
            
        elif opcion_panel == 5: 
            print("Sesión cerrada. Volviendo al menú anterior")
            salir = True  # Salir del panel de control
        else: 
            print("Opción ingresada inválida, intentá nuevamente.")
        
        # Cierra la conexión a la base de datos después de usarla
        conexion.close()