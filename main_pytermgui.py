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


GUI_VIDE = "~"
GUI_IMPACT = "X"
GUI_RATE = "o"


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


grille_solution, flotte = setup_jeu()

grille_joueur = Grille(grille_solution.lignes, grille_solution.nombre_colonnes)
nombre_coups = 0
bateaux_coules = 0


coups_label = ptg.Label(f"Coups: {nombre_coups}")
message_log = ptg.Label("Entrez vos coordonnées (ex: 3,5)")

player_grid_label = ptg.Label("")
input_field = ptg.InputField(prompt="Tir (x,y): ")


def generer_texte_grille(grille):
    texte = ""
    for y in range(grille.lignes):
        ligne_chars = []
        for x in range(grille.nombre_colonnes):
            char = grille.matrice[grille._index(x, y)]
            if char == grille.vide:
                ligne_chars.append(f" {GUI_VIDE} ")
            elif char in [GUI_IMPACT, GUI_RATE]:
                ligne_chars.append(f" {char} ")
            else: # C'est un bateau
                boat_char = "?"
                for b in flotte:
                    if (y,x) in b.positions:
                        boat_char = b.marque
                        break
                ligne_chars.append(f" {boat_char} ")
        texte += "".join(ligne_chars) + "\n"
    return texte

# --- Logique du jeu (appelée par le bouton "Tirer") ---
def on_submit_shot(btn):
    global nombre_coups, bateaux_coules
    
    entree = input_field.value     
    
    input_field.value = ""          
    
    try:
        x_str, y_str = entree.split(',')
        x, y = int(x_str.strip()), int(y_str.strip())
        
        if not (0 <= x < grille_joueur.nombre_colonnes and 0 <= y < grille_joueur.lignes):
            message_log.value = "Erreur: Coordonnées hors grille."
            return

        if grille_joueur.matrice[grille_joueur._index(x, y)] != grille_joueur.vide:
            message_log.value = "Erreur: Vous avez déjà tiré ici."
            return
            
    except Exception:
        message_log.value = "Erreur: Format invalide (doit être x,y)"
        return

    nombre_coups += 1
    coups_label.value = f"Coups: {nombre_coups}"
    
    case_visee = grille_solution.matrice[grille_solution._index(x, y)]

    if case_visee != grille_solution.vide:
        grille_joueur.matrice[grille_joueur._index(x, y)] = GUI_IMPACT
        message_log.value = f"Tir en ({x}, {y}) : TOUCHÉ !"
        
        bateau_touche = next(b for b in flotte if (y, x) in b.positions)
 
        coule = True
        for (pos_y, pos_x) in bateau_touche.positions:
            if grille_joueur.matrice[grille_joueur._index(pos_x, pos_y)] != GUI_IMPACT:
                coule = False
                break
        
        if coule:
            bateaux_coules += 1
            nom_bateau = bateau_touche.__class__.__name__
            message_log.value = f">>> {nom_bateau.upper()} COULÉ ! <<<"

            for (pos_y, pos_x) in bateau_touche.positions:
                grille_joueur.matrice[grille_joueur._index(pos_x, pos_y)] = bateau_touche.marque
    else:
        grille_joueur.matrice[grille_joueur._index(x, y)] = GUI_RATE
        message_log.value = f"Tir en ({x}, {y}) : Dans l'eau."


    player_grid_label.value = generer_texte_grille(grille_joueur)

    if bateaux_coules == len(flotte):
        message_log.value = f"Bravo ! Flotte coulée en {nombre_coups} coups."
        input_field.disabled = True
        btn.onclick = None

solution_text = generer_texte_grille(grille_solution)
player_grid_label.value = generer_texte_grille(grille_joueur)
submit_button = ptg.Button("Tirer !", onclick=on_submit_shot)

# --- MISE EN PAGE STABLE (VERTICALE) ---
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
                    ptg.Label("[bold]Grille du Joueur[/bold]"),
                    player_grid_label, # Le label qui sera mis à jour
                    box="DOUBLE",
                ),
            ),
            "",
            ptg.Splitter(input_field, submit_button),
            "",
            ptg.Splitter(coups_label, message_log),
            box="HEAVY"
        )
        .center()
    )
    manager.add(window)