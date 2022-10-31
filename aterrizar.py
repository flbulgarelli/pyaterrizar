class Cliente:
    pass

# patrón state (Estado)
class Libre:
    def esta_vendido(self): 
        return False

    def esta_reservado(self):
        return False

    def vender_a(self, asiento, cliente):
        asiento.comprador = cliente
        asiento.estado = Vendido()

class Vendido:
    def esta_vendido(self): 
        return True

    def esta_reservado(self):
        return False

    def vender_a(self, asiento, cliente):
        asiento.reservante = cliente
        asiento.estado = Reservado()

class Reservado:
    def esta_vendido(self): 
        return True

    def esta_reservado(self):
        return True

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
        return self.estado.esta_vendido()

    def reservado_a(self, cliente):
        return self.reservante == cliente

    def esta_reservado(self):
        return self.estado.esta_reservado()

    def liberar_reservas(self):
        pass
