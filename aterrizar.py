class Cliente:
    pass

class Asiento:
    def __init__(self):
        self.comprador = None

    def venderse(self, cliente):
        self.comprador = cliente

    def vendido_a(self, cliente):
        return self.comprador == cliente

    def esta_vendido(self):
        return self.comprador is not None