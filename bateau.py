class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    @property
    def positions(self):
        pos = []
        for i in range(self.longueur):
            if self.vertical:
                pos.append((self.ligne + i, self.colonne))
            else:
                pos.append((self.ligne, self.colonne + i))
        return pos
    
    def coule(self, grille):
        for y, x in self.positions:
            idx = y * grille.nombre_colonnes + x
            if grille.matrice[idx] != grille.touche:
                return False
        return True
