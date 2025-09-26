import pytest
from bateau import Bateau


def test_bateau_defaults():
    b = Bateau(2, 3)
    assert b.ligne == 2
    assert b.colonne == 3
    assert b.longueur == 1
    assert b.vertical is False


def test_bateau_custom():
    b = Bateau(1, 1, longueur=4, vertical=True)
    assert b.ligne == 1
    assert b.colonne == 1
    assert b.longueur == 4
    assert b.vertical is True
