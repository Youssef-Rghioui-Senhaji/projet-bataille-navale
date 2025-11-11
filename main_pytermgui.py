import pytermgui as ptg
import random


from grille import Grille
from bateau import Bateau

class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical)
        self.marque = "P"

class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical)
        self.marque = "C"

class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "T"

class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "S"

# --- Symboles ASCII sûrs ---
GUI_VIDE = "~"
GUI_IMPACT = "X"
GUI_RATE = "o"

# --- Fonction de configuration (inchangée) ---
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
            chevauchement = any(pos in autre.positions for pos in bateau.positions for autre in bateaux_places)
            if not chevauchement:
                placement_valide = True
        grille.ajoute(bateau)
        bateaux_places.append(bateau)
    return grille, flotte

# --- Variables globales du jeu ---
grille_solution, flotte = setup_jeu()
nombre_coups = 0
bateaux_coules = 0
player_grid_buttons = [] 
player_grid_rows_for_display = [] 
coups_label = ptg.Label("Coups: 0")
message_log = ptg.Label("En attente de votre premier tir...")
