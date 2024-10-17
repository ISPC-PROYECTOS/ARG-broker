class cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print("Titular: ", self.titular)
        print("Cantidad: ", self.cantidad)  
        
