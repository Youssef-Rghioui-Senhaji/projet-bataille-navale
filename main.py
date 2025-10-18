from grille import Grille
from porte_avion import PorteAvion
from croiseur import Croiseur
from torpilleur import Torpilleur
from sous_marin import SousMarin
from bateau import Bateau
import random

def clear_screen():
    """Efface le terminal pour une meilleure lisibilité."""
    os.system('cls' if os.name == 'nt' else 'clear')

def setup_jeu():
    """Initialise la grille et place les bateaux de manière aléatoire."""
    grille = Grille(lignes=8, colonnes=10)
    
    # Création de la flotte sans position initiale
    flotte = [
        PorteAvion(0, 0),
        Croiseur(0, 0),
        Torpilleur(0, 0),
        SousMarin(0, 0)
    ]
    
    bateaux_places = []

    for bateau in flotte:
        placement_valide = False
        while not placement_valide:
            # Choisir une orientation et une position de départ au hasard
            bateau.vertical = random.choice([True, False])
            if bateau.vertical:
                bateau.ligne = random.randint(0, grille.lignes - bateau.longueur)
                bateau.colonne = random.randint(0, grille.nombre_colonnes - 1)
            else:
                bateau.ligne = random.randint(0, grille.lignes - 1)
                bateau.colonne = random.randint(0, grille.nombre_colonnes - bateau.longueur)

            # Vérifier si le placement est valide (pas de chevauchement)
            chevauchement = False
            for pos in bateau.positions:
                for autre_bateau in bateaux_places:
                    if pos in autre_bateau.positions:
                        chevauchement = True
                        break
                if chevauchement:
                    break
            
            if not chevauchement:
                placement_valide = True

        # Une fois un placement valide trouvé, on l'ajoute à la grille et à notre liste
        grille.ajoute(bateau)
        bateaux_places.append(bateau)
    
    # Retourne la grille de jeu et la liste des bateaux placés
    return grille, bateaux_places

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
            if grille.matrice[idx] == "💣":
                for bateau in bateaux:
                    if (y, x) in bateau.positions:
                        grille.matrice[idx] = bateau.marque
                        print(f"🔥 Bateau coulé ! {type(bateau).__name__} ({bateau.marque})")
                        bateaux.remove(bateau)
                        
            else:
                print("💣 Touché !")
                grille.matrice[idx] = "💣"

            grille.afficher()  

        else:
            print("🔹 Eau")
            grille.tirer(x, y)

    print(f"\n🎉 Félicitations ! Vous avez coulé tous les bateaux en {coups} coups.")

if __name__ == "__main__":
    jeu()