import pytest
from grille import Grille


def test_init():
    g = Grille(5, 8)
    assert g.lignes == 5
    assert g.colonnes == 8
    assert len(g.matrice) == 5
    assert len(g.matrice[0]) == 8
