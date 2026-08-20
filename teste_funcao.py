from funcao import multiplicar

def test_multi_positivo():
    assert multiplicar(5,6) == 30

def test_multi_negativo():
    assert multiplicar(-5,-6) == 30

def test_multi_negpos():
    assert multiplicar(-5,6) == -30

