from grille import Grille

grille = Grille(5, 8)

while True:

    grille.afficher()

    try:
        x = int(input("Entrez la colonne (x) : "))
        y = int(input("Entrez la ligne (y) : "))
    except ValueError:
        print("Veuillez entrer des nombres valides.")
        continue

    if not (0 <= x < grille.colonnes) or not (0 <= y < grille.lignes):
        print("Coordonnées hors de la grille, réessayez.")
        continue

    grille.tirer(x, y)
