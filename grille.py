class Grille:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.nombre_colonnes = colonnes
        self.vide = "∿"
        self.rate = "x"
        self.impact = "💣"
        self.bateau = "⛵"
        self.matrice = [self.vide for _ in range(lignes * colonnes)]

    def _index(self, x, y):
        if not (0 <= x < self.nombre_colonnes and 0 <= y < self.lignes):
            raise IndexError("Coordonnées hors de la grille")
        return y * self.nombre_colonnes + x

    def afficher(self):
        for y in range(self.lignes):
            ligne = []
            for x in range(self.nombre_colonnes):
                ligne.append(self.matrice[self._index(x, y)])
            print(" ".join(ligne))

    def tirer(self, x, y, touche=None):
        if touche is None:
            touche = self.rate
        idx = self._index(x, y)
        self.matrice[idx] = touche
        return True

    def ajoute(self, bateau):
        for (y, x) in bateau.positions:
            if x >= self.nombre_colonnes or y >= self.lignes:
                return False  
        for (y, x) in bateau.positions:
            idx = self._index(x, y)
            self.matrice[idx] = getattr(bateau, "marque", self.bateau)
        return True
        
    def afficher_corrige(self):
        for l in range(self.lignes):
            ligne = ""
            for c in range(self.nombre_colonnes):
                idx = l * self.nombre_colonnes + c
                case = self.matrice[idx]
                # Si la case contient un bateau, on affiche sa marque directement
                if isinstance(case, str) and case not in [self.vide, "x", "💣"]:
                    ligne += case
                else:
                    ligne += case
            print(ligne)

