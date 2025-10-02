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
                    if vertical:
                        if y + bateau.longueur > grille.lignes:
                            continue
                    else:
                        if x + bateau.longueur > grille.nombre_colonnes:
                            continue

                    chevauchement = False
                    for y_, x_ in bateau.positions:
                        idx = y_ * grille.nombre_colonnes + x_
                        if grille.matrice[idx] != grille.vide:
                            chevauchement = True
                            break
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

        coups += 1
        idx = y * grille.nombre_colonnes + x
        case = grille.matrice[idx]

        if case in [bateau.marque for bateau in bateaux if hasattr(bateau, "marque")]:
            print("💣 Touché !")
            grille.tirer(x, y, touche="💣")
        elif case == "💣" or case == "x":
            print("Vous avez déjà tiré ici !")
        else:
            print("🔹 Eau")
            grille.tirer(x, y)

        for bateau in bateaux[:]:
            if bateau.coule(grille):
                print(f"Bateau coulé ! {type(bateau).__name__} ({bateau.marque})")
                for y_, x_ in bateau.positions:
                    grille.tirer(x_, y_, touche=bateau.marque)
                bateaux.remove(bateau)

    print(f"Félicitations ! Vous avez coulé tous les bateaux en {coups} coups.")
if __name__ == "__main__":
    jeu()