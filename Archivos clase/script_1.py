class vehiculo ():

    def arrancar (self):
        print("Arrancando vehiculo")


class carro(vehiculo):
    
    def __init__(self) -> None:
        print("Carro creado")

    def acelerar (self):
        print("Acelerando.....")

    def frenar (self):
        print("Frenando.....")

class bicicleta(vehiculo):
    
    def __init__(self, numero_llantas=2) -> None:
        self.llantas = numero_llantas

    def arrancar(self):
        print("Pedaleando..." + str(self.llantas))

    def acelerar (self):
        print("Acelerando.....")

    def frenar (self):
        print("Frenando.....")

mazda = bicicleta()

mazda.arrancar()
mazda.acelerar()
mazda.frenar()
