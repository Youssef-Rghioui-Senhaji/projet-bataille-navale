import pytest
from grille import Grille


def test_init():
    g = Grille(5, 8)
    assert g.lignes == 5
    assert g.nombre_colonnes == 8
    assert len(g.matrice) == 5 * 8
    assert all(cell == g.vide for cell in g.matrice)


def test_tirer():
    g = Grille(3, 4)
    idx0 = 0 * g.nombre_colonnes + 0
    assert g.matrice[idx0] == g.vide

    res = g.tirer(0, 0)
    assert res is True
    assert g.matrice[idx0] == g.rate

    idx2 = 1 * g.nombre_colonnes + 2
    g.tirer(2, 1)
    assert g.matrice[idx2] == g.rate


def test_afficher(capsys):
    g = Grille(2, 2)
    g.tirer(0, 0)
    g.afficher()
    captured = capsys.readouterr()
    assert g.rate in captured.out
    assert g.vide in captured.out

def test_tirer_personnalise():
    g = Grille(2, 2)

    g.tirer(0, 0, touche=g.impact)
    idx = 0 * g.nombre_colonnes + 0
    assert g.matrice[idx] == g.impact

    g.tirer(1, 1, touche="💥")
    idx2 = 1 * g.nombre_colonnes + 1
    assert g.matrice[idx2] == "💥"