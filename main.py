from grille import Grille
from porte_avion import PorteAvion
from croiseur import Croiseur
from torpilleur import Torpilleur
from sous_marin import SousMarin
from bateau import Bateau
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def setup_jeu():
    grille = Grille(lignes=8, colonnes=10)
    
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

            bateau.vertical = random.choice([True, False])
            if bateau.vertical:
                bateau.ligne = random.randint(0, grille.lignes - bateau.longueur)
                bateau.colonne = random.randint(0, grille.nombre_colonnes - 1)
            else:
                bateau.ligne = random.randint(0, grille.lignes - 1)
                bateau.colonne = random.randint(0, grille.nombre_colonnes - bateau.longueur)


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


        grille.ajoute(bateau)
        bateaux_places.append(bateau)
    

    return grille, bateaux_places

def main():
    
    grille_jeu, flotte = setup_jeu()
    
    grille_joueur = Grille(grille_jeu.lignes, grille_jeu.nombre_colonnes)
    
    nombre_coups = 0
    bateaux_coules = 0
    
    print("--- SOLUTION (POUR LA CORRECTION) ---")
    grille_jeu.afficher()
    print("-" * 30)
    
    # --- Boucle de jeu principale ---
    while bateaux_coules < len(flotte):
        print("\n--- GRILLE DU JOUEUR ---")
        grille_joueur.afficher()
        
        saisie_valide = False
        while not saisie_valide:
            try:
                entree = input("\nEntrez les coordonnées du tir max[9,7] (ex: 'colonne,ligne'): ")
                x_str, y_str = entree.split(',')
                x, y = int(x_str.strip()), int(y_str.strip())
                
                if not (0 <= x < grille_joueur.nombre_colonnes and 0 <= y < grille_joueur.lignes):
                    print("Erreur : Coordonnées hors de la grille. Réessayez.")
                    continue

                if grille_joueur.matrice[grille_joueur._index(x, y)] != grille_joueur.vide:
                    print("Erreur : Vous avez déjà tiré sur cette case. Réessayez.")
                    continue
                
                saisie_valide = True

            except ValueError:
                print("Erreur de format. Veuillez entrer les coordonnées sous la forme 'colonne,ligne'.")
            except Exception as e:
                print(f"Une erreur inattendue est survenue: {e}")

        nombre_coups += 1
        
        case_visee_solution = grille_jeu.matrice[grille_jeu._index(x, y)]

        if case_visee_solution not in [grille_jeu.vide, "x", "💣"]:
            print("\n>>> TOUCHÉ ! <<<")
            grille_joueur.tirer(x, y, touche=grille_joueur.impact)
            
            bateau_touche = None
            for bateau in flotte:
                if (y, x) in bateau.positions:
                    bateau_touche = bateau
                    break
            
            if bateau_touche and bateau_touche.coule(grille_joueur):
                bateaux_coules += 1
                nom_bateau = bateau_touche.__class__.__name__
                print(f"\n>>> {nom_bateau.upper()} COULÉ ! <<<")
                
                for pos_y, pos_x in bateau_touche.positions:
                    grille_joueur.matrice[grille_joueur._index(pos_x, pos_y)] = bateau_touche.marque

        else:
            print("\n>>> DANS L'EAU ! <<<")
            grille_joueur.tirer(x, y, touche=grille_joueur.rate)

    # --- Fin de la partie ---
    clear_screen()
    print("--- PARTIE TERMINÉE ---")
    print("\nFélicitations, vous avez coulé toute la flotte !")
    print(f"Votre score : {nombre_coups} coups.")
    
    print("\nGrille finale :")
    grille_joueur.afficher()


# Lancer le jeu
if __name__ == "__main__":
    main()