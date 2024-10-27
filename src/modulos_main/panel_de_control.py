from src.dao.portafolio_dao import PortafolioDAO
from src.util.conexion_bd import obtener_conexion
from src.dao.cotizacion_dao import CotizacionDAO
from src.models.transaccion_model import Transaccion
from datetime import datetime


def mostrar_menu():
    print('-----> PANEL DE CONTROL <-----')
    print("1. Ver mi Saldo.")
    print("2. Historial de transacciones y sus rendimientos.")
    print("3. Comprar.")
    print("4. Vender.")
    print("5. Cerrar sesión.")


def ver_saldo(conexion, cuit_inversor):
    portafolio_dao = PortafolioDAO(conexion)
    saldo = portafolio_dao.obtener_suma_transacciones(cuit_inversor)
    print(f"Saldo total: {saldo:.2f}")


def ver_historial_transacciones(conexion, cuit_inversor):
    portafolio_dao = PortafolioDAO(conexion)
    transacciones = portafolio_dao.obtener_transacciones(cuit_inversor)

    if transacciones:
        print("\n---- Historial de Transacciones ----")
        print(f"{'ID':<10} {'Tipo':<10} {'CUIT/CUIL':<15} {'Acción':<15} {'Cantidad':<10} {'Fecha':<20} {'Valor':<10}")
        print("-" * 90)

        for transaccion in transacciones:
            tipo_transaccion = "Compra" if transaccion['id_tipo_transaccion'] == 1 else "Venta"
            fecha = transaccion['fecha_hora_transaccion'].strftime('%Y-%m-%d %H:%M')
            print(f"{transaccion['id_num_transaccion']:<10} {tipo_transaccion:<10} {transaccion['cuit_o_cuil']:<15} "
                  f"{transaccion['id_cotizacion_accion']:<15} {transaccion['cantidad_acciones_transaccion']:<10} "
                  f"{fecha:<20} {transaccion['valor_transaccion']:<10}")
        print("-" * 90)
    else:
        print("No hay transacciones para mostrar.")


def realizar_compra(conexion, cuit_inversor):
    cotizacion_dao = CotizacionDAO(conexion)
    cotizaciones = cotizacion_dao.obtener_cotizaciones()

    if not cotizaciones:
        print("No hay cotizaciones disponibles.")
        return

    print(f"{'Nombre':<40} {'Símbolo':<10} {'Fecha y Hora':<20} {'Precio Venta':<15} {'Precio Compra':<15} {'Cantidad Disponible':<20}")
    print("=" * 130)

    for cotizacion in cotizaciones:
        fecha_hora = datetime.strptime(cotizacion.get_fecha_hora(), '%Y-%m-%d %H:%M:%S')
        print(f"{cotizacion.get_nombre():<40} {cotizacion.get_simbolo():<10} "
              f"{fecha_hora.strftime('%Y-%m-%d %H:%M:%S'):<20} {cotizacion.get_precio_venta():<15.2f} "
              f"{cotizacion.get_precio_compra():<15.2f} {cotizacion.get_cantidad_disponible():<20}")

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

def realizar_venta(conexion, cuit_inversor):
    portafolio_dao = PortafolioDAO(conexion)
    transacciones = portafolio_dao.obtener_transacciones(cuit_inversor)

    if not transacciones:
        print("No hay transacciones para mostrar.")
        return

    ver_historial_transacciones(conexion, cuit_inversor)

    id_accion = int(input("Ingrese el ID de la acción que desea vender: "))
    cantidad_a_vender = int(input("Ingrese la cantidad de acciones que desea vender: "))

    transaccion_seleccionada = next((trans for trans in transacciones if trans['id_num_transaccion'] == id_accion), None)

    if transaccion_seleccionada:
        cantidad_total_comprada = sum(
            trans['cantidad_acciones_transaccion']
            for trans in transacciones
            if trans['id_cotizacion_accion'] == transaccion_seleccionada['id_cotizacion_accion'] and trans['id_tipo_transaccion'] == 1  # Solo compras
        )

        print(f"Cantidad disponible para vender de ID {id_accion}: {cantidad_total_comprada} acciones.")

        if cantidad_a_vender <= cantidad_total_comprada:
            print(f"Venta exitosa. Cantidad vendida: {cantidad_a_vender} acciones del ID {id_accion}.")
        else:
            print("No tiene suficientes acciones para vender la cantidad solicitada.")
    else:
        print("ID de acción no válido. Por favor, inténtelo nuevamente.")


def panel_de_control(email_inversor, cuit_inversor):
    salir = False
    while not salir:
        mostrar_menu()
        opcion_panel = int(input("Ingrese la opción elegida: "))

        conexion = obtener_conexion()

        if opcion_panel == 1:
            ver_saldo(conexion, cuit_inversor)
        elif opcion_panel == 2:
            ver_historial_transacciones(conexion, cuit_inversor)
        elif opcion_panel == 3:
            realizar_compra(conexion, cuit_inversor)
        elif opcion_panel == 4:
            realizar_venta(conexion, cuit_inversor)
        elif opcion_panel == 5:
            print("Sesión cerrada. Volviendo al menú anterior.")
            salir = True
        else:
            print("Opción ingresada inválida, intentá nuevamente.")

        conexion.close()