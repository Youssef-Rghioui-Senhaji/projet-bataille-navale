import pytest
from grille import Grille


def test_init():
    g = Grille(5, 8)
    assert g.lignes == 5
    assert g.colonnes == 8
    assert len(g.matrice) == 5
    assert len(g.matrice[0]) == 8




def test_afficher(capsys):
    g = Grille(2, 2)
    g.tirer(0, 0)
    g.afficher()
    captured = capsys.readouterr()
    assert "X" in captured.out
    assert "." in captured.out

