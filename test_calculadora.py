from calculadora import restar, sumar

def test_sum():
    assert sumar(2, 3) == 5

def test_restar():
    assert restar(5, 3) == 2