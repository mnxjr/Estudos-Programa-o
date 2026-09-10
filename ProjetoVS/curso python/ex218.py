class Carro:
    def __init__(self, name):
        self.name = name
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, value):
        self._motor = value

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, value):
        self._fabricante = value


class Fabricante:
    def __init__(self, name):
        self.name = name

class Motor:
    def __init__(self, name):
        self.name = name

    
Fiat = Fabricante('Fiat')
fire1_0 = Motor('Fire 1.0')
Ciena = Carro('Ciena')
Ciena.fabricante = Fiat
Ciena.motor = fire1_0
print(Ciena.name, Ciena.fabricante.name, Ciena.motor.name)