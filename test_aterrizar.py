from aterrizar import *

def test_a48_puede_venderse_a_ro():
    ro = Cliente()
    a48 = Asiento()

    a48.venderse(ro)

    assert a48.vendido_a(ro)
    assert a48.esta_vendido()


def test_si_a48_no_se_vende_no_esta_vendido():
    ro = Cliente()
    a48 = Asiento()

    assert not a48.vendido_a(ro)
    assert not a48.esta_vendido()