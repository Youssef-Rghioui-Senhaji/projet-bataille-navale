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

# --- Logique du jeu lors d'un clic ---
def on_grid_click(button: ptg.Button, x: int, y: int):
    """Gère le tir et met à jour l'interface."""
    global nombre_coups, bateaux_coules

    if button.label != grille_solution.vide:
        message_log.value = "Vous avez déjà tiré ici !"
        return

    nombre_coups += 1
    coups_label.value = f"Coups: {nombre_coups}"
    
    case_visee = grille_solution.matrice[grille_solution._index(x, y)]

    if case_visee != grille_solution.vide:
        button.label = grille_solution.impact
        message_log.value = f"Tir en ({x}, {y}) : TOUCHÉ !"
        bateau_touche = next(b for b in flotte if (y, x) in b.positions)
        
        positions_bateau_touche = [player_grid_buttons[pos_y][pos_x] for pos_y, pos_x in bateau_touche.positions]
        if all(btn.label == grille_solution.impact for btn in positions_bateau_touche):
            bateaux_coules += 1
            nom_bateau = bateau_touche.__class__.__name__
            message_log.value = f">>> {nom_bateau.upper()} COULÉ ! <<<"
            for btn in positions_bateau_touche:
                btn.label = bateau_touche.marque
    else:
        button.label = grille_solution.rate
        message_log.value = f"Tir en ({x}, {y}) : Dans l'eau."

    if bateaux_coules == len(flotte):
        message_log.value = f"Bravo ! Flotte coulée en {nombre_coups} coups."
        for row in player_grid_buttons:
            for btn in row:
                btn.onclick = None

# --- Préparation de tous les widgets avant de lancer le WindowManager ---
# 1. Grille du joueur : une liste de lignes, où chaque ligne est un Splitter de boutons
for y in range(grille_solution.lignes):
    buttons_in_row = []
    for x in range(grille_solution.nombre_colonnes):
        button = ptg.Button(
            label=grille_solution.vide,
            onclick=lambda btn, cx=x, cy=y: on_grid_click(btn, cx, cy)
        )
        buttons_in_row.append(button)
    player_grid_buttons.append(ptg.Splitter(*buttons_in_row)) # Chaque ligne est un Splitter

# 2. Grille solution : un simple texte
solution_text = ""
for y in range(grille_solution.lignes):
    ligne = [grille_solution.matrice[grille_solution._index(x, y)] for x in range(grille_solution.nombre_colonnes)]
    solution_text += " ".join(ligne) + "\n"

# 3. On assemble les widgets dans une fenêtre
with ptg.WindowManager() as manager:
    window = (
        ptg.Window(
            ptg.Label("[bold]BATAILLE NAVALE[/bold]", parent_align=0),
            "",
            ptg.Splitter(
                ptg.Container(
                    ptg.Label("[bold]Grille Solution[/bold]"),
                    ptg.Label(solution_text),
                    box="DOUBLE",
                ),
                ptg.Container(
                    ptg.Label("[bold]Grille du Joueur (Cliquez)[/bold]"),
                    # On ajoute directement les lignes de boutons ici
                    *player_grid_buttons,
                    box="DOUBLE",
                ),
            ),
            "",
            ptg.Splitter(coups_label, message_log),
            box="HEAVY"
        )
        .center()
    )
    manager.add(window)