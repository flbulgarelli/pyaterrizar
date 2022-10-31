from aterrizar import *

def test_a48_puede_venderse_a_ro():
    ro = Cliente()
    a48 = Asiento()

    a48.venderse(ro)

    assert a48.vendido_a(ro)