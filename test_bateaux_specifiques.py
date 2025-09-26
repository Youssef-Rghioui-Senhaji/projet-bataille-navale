import pytest
from grille import Grille
from porte_avion import PorteAvion
from croiseur import Croiseur
from torpilleur import Torpilleur
from sous_marin import SousMarin


def test_marque_bateau():
    g = Grille(5, 5)

    pa = PorteAvion(0, 0)
    cro = Croiseur(1, 1)
    tor = Torpilleur(3, 0)
    sub = SousMarin(4, 3)

    g.ajoute(pa)
    g.ajoute(cro)
    g.ajoute(tor)
    g.ajoute(sub)

    assert g.matrice[0] == "🚢"  
    assert g.matrice[6] == "⛴"  
    assert g.matrice[15] == "🚣"  
    assert g.matrice[23] == "🐟"  
