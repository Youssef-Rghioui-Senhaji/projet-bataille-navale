class Grille:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.nombre_colonnes = colonnes
        self.vide = "∿"
        self.touche = "x"
        self.matrice = [self.vide for _ in range(lignes * colonnes)]

    def afficher(self):
        for y in range(self.lignes):
            ligne = []
            for x in range(self.nombre_colonnes):
                ligne.append(self.matrice[self._index(x, y)])
            print(" ".join(ligne))

    def _index(self, x, y):
        return y * self.nombre_colonnes + x

    def tirer(self, x, y):
        idx = self._index(x, y)
        self.matrice[idx] = self.touche
        return True
