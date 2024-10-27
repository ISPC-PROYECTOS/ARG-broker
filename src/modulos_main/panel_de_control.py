from src.dao.portafolio_dao import PortafolioDAO
from src.util.conexion_bd import obtener_conexion
from src.dao.cotizacion_dao import CotizacionDAO
from src.models.transaccion_model import Transaccion
from src.dao.transaccion_dao import TransaccionDAO
from datetime import datetime

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
            cotizacion_dao = CotizacionDAO(conexion)
            cotizaciones = cotizacion_dao.obtener_cotizaciones()

            print(f"{'Nombre':<40} {'Símbolo':<10} {'Fecha y Hora':<20} {'Precio Venta':<15} {'Precio Compra':<15} {'Cantidad Disponible':<20}")
            print("=" * 130)

            if cotizaciones:  
                for cotizacion in cotizaciones:
                    fecha_hora_str = cotizacion.get_fecha_hora()  
                    fecha_hora = datetime.strptime(fecha_hora_str, '%Y-%m-%d %H:%M:%S') if isinstance(fecha_hora_str, str) else fecha_hora_str
                    
                    print(f"{cotizacion.get_nombre():<40} {cotizacion.get_simbolo():<10} {fecha_hora.strftime('%Y-%m-%d %H:%M:%S'):<20} {cotizacion.get_precio_venta():<15.2f} {cotizacion.get_precio_compra():<15.2f} {cotizacion.get_cantidad_disponible():<20}")

                simbolo = input("Ingrese el símbolo de la acción que desea comprar: ")
                cantidad = int(input("Ingrese la cantidad de acciones que desea comprar: "))

                portafolio_dao = PortafolioDAO(conexion)
                saldo_disponible = portafolio_dao.obtener_suma_transacciones(cuit_inversor)

                cotizacion_seleccionada = next((c for c in cotizaciones if c.get_simbolo() == simbolo), None)

                if cotizacion_seleccionada:
                    transaccion = Transaccion(cotizacion_seleccionada.get_nombre(), 0, cotizacion_seleccionada.get_precio_compra())
                    resultado_compra = transaccion.comprar(cantidad, saldo_disponible)

                    print(resultado_compra)  
                else:
                    print("El símbolo ingresado no corresponde a ninguna cotización disponible.")
            else:
                print("No hay cotizaciones disponibles.")   

        elif opcion_panel == 4: 
            print("Vender acciones")
            
        elif opcion_panel == 5: 
            print("Sesión cerrada. Volviendo al menú anterior")
            salir = True  
        else: 
            print("Opción ingresada inválida, intentá nuevamente.")
        
        conexion.close()