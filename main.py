from grille import Grille
from porte_avion import PorteAvion
from croiseur import Croiseur
from torpilleur import Torpilleur
from sous_marin import SousMarin
from bateau import Bateau
import random


def placer_bateaux_aleatoirement(grille, bateaux):
    for bateau in bateaux:
        positions_possibles = []

        for y in range(grille.lignes):
            for x in range(grille.nombre_colonnes):
                for vertical in [False, True]:
                    bateau_test = type(bateau)(y, x, vertical)
                    if not grille.ajoute(bateau_test):
                        continue
                    chevauchement = any(
                        grille.matrice[y_ * grille.nombre_colonnes + x_] != grille.vide
                        for y_, x_ in bateau_test.positions
                    )
                    if not chevauchement:
                        positions_possibles.append((y, x, vertical))

        if positions_possibles:
            y, x, vertical = random.choice(positions_possibles)
            bateau.ligne = y
            bateau.colonne = x
            bateau.vertical = vertical
            grille.ajoute(bateau)


def jeu():
    grille = Grille(8, 10)
    bateaux = [PorteAvion(0, 0), Croiseur(0, 0), Torpilleur(0, 0), SousMarin(0, 0)]

    placer_bateaux_aleatoirement(grille, bateaux)

    coups = 0
    while bateaux:
        grille.afficher()
        try:
            x = int(input("Colonne à tirer (0-9) : "))
            y = int(input("Ligne à tirer (0-7) : "))
        except ValueError:
            print("Veuillez entrer des nombres valides")
            continue


