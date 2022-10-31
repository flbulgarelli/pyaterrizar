class Cliente:
    pass

class Libre:
    def vender_a(self, asiento, cliente):
        asiento.comprador = cliente
        asiento.estado = Vendido()

class Vendido:
    def vender_a(self, asiento, cliente):
        asiento.reservante = cliente
        asiento.estado = Reservado()

class Reservado:
    def vender_a(self, asiento, cliente):
        # asiento.estado = Sobrereservador()
        pass

class Asiento:
    def __init__(self):
        self.comprador = None
        self.estado = Libre()

    def venderse(self, cliente):
        self.estado.vender_a(self, cliente)

    def vendido_a(self, cliente):
        return self.comprador == cliente

    def esta_vendido(self):
        return self.comprador is not None

    def reservado_a(self, cliente):
        return self.reservante == cliente

    def esta_reservado(self):
        return self.reservante is not None
