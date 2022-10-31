from aterrizar import *

ro = None
ana = None
a48 = None

def setup_function():
    global ro
    global ana
    global a48
    ro = Cliente()
    ana = Cliente()
    a48 = Asiento()

def test_a48_puede_venderse_a_ro():    
    a48.venderse(ro)

    assert a48.vendido_a(ro)
    assert a48.esta_vendido()


def test_si_a48_no_se_vende_no_esta_vendido():
    assert not a48.vendido_a(ro)
    assert not a48.esta_vendido()


def test_si_viene_ana_y_compra_un_asiento_vendido_no_se_vende():
    a48.venderse(ro)
    a48.venderse(ana)

    assert a48.vendido_a(ro)
    assert not a48.vendido_a(ana)


def test_si_viene_ana_y_compra_un_asiento_vendido_se_reserva():
    a48.venderse(ro)
    a48.venderse(ana)

    assert a48.reservado_a(ana)
    assert a48.esta_reservado()
