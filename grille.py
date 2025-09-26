class Grille:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.matrice = [[0 for _ in range(colonnes)] for _ in range(lignes)]
