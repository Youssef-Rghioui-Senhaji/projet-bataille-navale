class Grille:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.nombre_colonnes = colonnes
        self.matrice = [0 for _ in range(lignes * colonnes)]

    def afficher(self):
        for row in self.matrice:
            print(" ".join("X" if cell else "." for cell in row))

    def _index(self, x, y):
        return y * self.nombre_colonnes + x

    def tirer(self, x, y):
        self.matrice[y][x] = 1
