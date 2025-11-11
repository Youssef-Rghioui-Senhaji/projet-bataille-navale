import pytermgui as ptg
import random

from grille import Grille
from porte_avion import PorteAvion
from croiseur import Croiseur
from torpilleur import Torpilleur
from sous_marin import SousMarin


def setup_jeu():

    grille = Grille(lignes=8, colonnes=10)
    flotte = [PorteAvion(0, 0), Croiseur(0, 0), Torpilleur(0, 0), SousMarin(0, 0)]
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

            chevauchement = any(pos in autre_bateau.positions for pos in bateau.positions for autre_bateau in bateaux_places)
            
            if not chevauchement:
                placement_valide = True

        grille.ajoute(bateau)
        bateaux_places.append(bateau)
    
    return grille, bateaux_places


grille_solution, flotte = setup_jeu()
nombre_coups = 0
bateaux_coules = 0
player_grid_buttons = []


coups_label = ptg.Label("Coups: 0")
message_log = ptg.Label("En attente de votre premier tir...")

