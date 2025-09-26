import pytest
from bateau import Bateau
from grille import Grille


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


def test_bateau_positions_horizontal():
    b = Bateau(2, 3, longueur=3)
    assert b.positions == [(2, 3), (2, 4), (2, 5)]


def test_bateau_positions_vertical():
    b = Bateau(2, 3, longueur=3, vertical=True)
    assert b.positions == [(2, 3), (3, 3), (4, 3)]


def test_ajoute_bateau():
    g = Grille(2, 3)

    b1 = Bateau(1, 0, longueur=2, vertical=False)
    assert g.ajoute(b1) is True
    assert g.matrice == ["∿", "∿", "∿", "⛵", "⛵", "∿"]

    b2 = Bateau(1, 0, longueur=2, vertical=True)
    assert g.ajoute(b2) is False
    assert g.matrice == ["∿", "∿", "∿", "⛵", "⛵", "∿"]

    b3 = Bateau(1, 0, longueur=4, vertical=True)
    assert g.ajoute(b3) is False
    assert g.matrice == ["∿", "∿", "∿", "⛵", "⛵", "∿"]
