import estoesunaprueba as estoesunaprueba


def test_pruebas():
    assert estoesunaprueba.suma(4, 1) == 5
    assert estoesunaprueba.resta(5, 1) == 4
    assert estoesunaprueba.resta(-3, 1) == -4
    assert estoesunaprueba.resta(-9, 1) == -10
    assert estoesunaprueba.suma(5, 1) == 6
    assert estoesunaprueba.suma(5, -2) == 3
    assert estoesunaprueba.resta(5, -20) == 25
