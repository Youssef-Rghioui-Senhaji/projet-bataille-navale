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
                for vertical in (False, True):
                    if vertical:
                        if y + bateau.longueur > grille.lignes:
                            continue
                    else:
                        if x + bateau.longueur > grille.nombre_colonnes:
                            continue
                    candidate_positions = [
                        (y + i, x) if vertical else (y, x + i)
                        for i in range(bateau.longueur)
                    ]
                    occupied = False
                    for py, px in candidate_positions:
                        idx = py * grille.nombre_colonnes + px
                        if grille.matrice[idx] != grille.vide:
                            occupied = True
                            break
                    if not occupied:
                        positions_possibles.append((y, x, vertical))
        if positions_possibles:
            y, x, vertical = random.choice(positions_possibles)
            bateau.ligne = y
            bateau.colonne = x
            bateau.vertical = vertical
            grille.ajoute(bateau)

def afficher_joueur(grille, bateaux):
    marque_to_bateau = {getattr(b, "marque", None): b for b in bateaux if hasattr(b, "marque")}
    for y in range(grille.lignes):
        row = []
        for x in range(grille.nombre_colonnes):
            idx = y * grille.nombre_colonnes + x
            cell = grille.matrice[idx]
            if isinstance(cell, Bateau):
                row.append(grille.vide)  # Afficher vide pour les bateaux
            elif isinstance(cell, str) and cell in marque_to_bateau:
                bateau = marque_to_bateau[cell]
                row.append(grille.vide)  # Afficher vide pour les bateaux
            else:
                row.append(cell)
        print(" ".join(row))

def jeu():
    grille = Grille(8, 10)
    bateaux = [PorteAvion(0, 0), Croiseur(0, 0), Torpilleur(0, 0), SousMarin(0, 0)]

    placer_bateaux_aleatoirement(grille, bateaux)

    print("\n=== Grille avec placement des bateaux ===")
    grille.afficher_corrige()  # Afficher la grille avec les bateaux

    shots = set()
    coups = 0

    while bateaux:
        print("\n=== Grille joueur ===")
        afficher_joueur(grille, bateaux)

        try:
            x = int(input(f"Colonne à tirer (0-{grille.nombre_colonnes - 1}) : "))
            y = int(input(f"Ligne à tirer (0-{grille.lignes - 1}) : "))
        except ValueError:
            print("Veuillez entrer des nombres valides")
            continue

        if not (0 <= x < grille.nombre_colonnes and 0 <= y < grille.lignes):
            print("Coordonnées hors de la grille")
            continue

        if (x, y) in shots:
            idx = y * grille.nombre_colonnes + x
            if grille.matrice[idx] != "💣":
                print("Vous avez déjà tiré ici !")
                continue

        idx = y * grille.nombre_colonnes + x
        cell = grille.matrice[idx]

        marques = [getattr(b, "marque", None) for b in bateaux if hasattr(b, "marque")]
        is_hit = False
        if isinstance(cell, Bateau):
            is_hit = True
        elif isinstance(cell, str) and (cell in marques or cell == "💣"):
            is_hit = True

        shots.add((x, y))
        coups += 1

        if is_hit:
            print("💣 Touché !")
            for bateau in bateaux:
                if (y, x) in bateau.positions:
                    for (py, px) in bateau.positions:
                        pidx = py * grille.nombre_colonnes + px
                        grille.matrice[pidx] = bateau.marque
                    print(f"🔥 Bateau révélé : {type(bateau).__name__} ({bateau.marque})")
                    try:
                        bateaux.remove(bateau)
                    except ValueError:
                        pass
                    break
            grille.afficher()  # actualiser l'affichage
        else:
            print("🔹 Eau")
            grille.tirer(x, y)

        for bateau in bateaux[::]:
            if bateau.coule(grille):
                print(f"🔥 Bateau coulé ! {type(bateau).__name__} ({bateau.marque})")
                for (py, px) in bateau.positions:
                    pidx = py * grille.nombre_colonnes + px
                    grille.matrice[pidx] = bateau.marque
                bateaux.remove(bateau)

    print(f"\n🎉 Félicitations ! Vous avez coulé tous les bateaux en {coups} coups.")

if __name__ == "__main__":
    jeu()