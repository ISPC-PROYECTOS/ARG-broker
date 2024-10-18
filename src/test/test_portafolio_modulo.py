import pytest
from models.portafolio_model import Portafolio

def test_estado():
    portafolio=Portafolio()
    assert portafolio.get_estado()==True

def test_saldo():
    portafolio=Portafolio()
    assert portafolio.get_saldo_inicial()==1000000

def test_mostrar_saldo_cuenta():
    portafolio=Portafolio()
    assert portafolio.get_saldo_cuenta()==1000000


def test_mostrar_transacciones():
    portafolio = Portafolio()
    transacciones_ejemplo = ["Compra de acciones x", "Venta de bonosx"]
    portafolio.set_transacciones(transacciones_ejemplo)
    resultado = portafolio.mostrar_transacciones()
    
    assert resultado == f"Transacciones: {transacciones_ejemplo}"


@pytest.mark.parametrize("suma_precio_venta, suma_precio_compra, rendimiento", [
    (6000,7000,-1000),
    (5500,4000,1500),
    (8000,11000,-3000)   
])

def test_calcular_rendimiento(suma_precio_venta,suma_precio_compra,rendimiento):
    portafolio=Portafolio()
    assert portafolio.calcular_rendimiento(
        suma_precio_venta,suma_precio_compra)== rendimiento
    
def test_str():
    portafolio=Portafolio(rendimiento=6000)
    resultado_esperado= "Su resndiemiento actual es $60000"
    
    



    