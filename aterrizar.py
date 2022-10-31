class Cliente:
    pass

class Asiento:
    def venderse(self, cliente):
        self.comprador = cliente

    def vendido_a(self, cliente):
        return self.comprador == cliente