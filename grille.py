class Grille:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.matrice = [[0 for _ in range(colonnes)] for _ in range(lignes)]

    def afficher(self):
        for row in self.matrice:
            print(" ".join("X" if cell else "." for cell in row))

    def tirer(self, x, y):
        self.matrice[y][x] = 1
