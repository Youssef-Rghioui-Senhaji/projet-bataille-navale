🚢 Bataille Navale en Ligne de Commande
Ceci est un jeu de bataille navale simple développé en Python, entièrement jouable depuis un terminal. Le joueur affronte une flotte de bateaux placés aléatoirement sur une grille et doit les couler en un minimum de coups.

Ce projet a été réalisé en utilisant une approche orientée objet pour structurer le code de manière claire et modulaire.

🎮 Fonctionnalités
Grille de Jeu Dynamique : Le jeu se déroule sur une grille de 8 lignes par 10 colonnes.

Flotte Complète : Une flotte de 4 bateaux de types différents est présente :

1 Porte-Avion (4 cases)

1 Croiseur (3 cases)

1 Torpilleur (2 cases)

1 Sous-Marin (2 cases)

Placement Aléatoire : À chaque nouvelle partie, les bateaux sont placés aléatoirement sur la grille, avec la garantie qu'ils ne se chevauchent jamais.

Interface Intuitive : Le jeu se contrôle facilement en entrant des coordonnées (x,y) dans le terminal.

Feedback Visuel Clair :

💣 : Tir réussi (touché)

x : Tir manqué (dans l'eau)

🚢, ⛴, 🚣, 🐟 : Bateau révélé une fois coulé

Comptage des Points : Le nombre de tirs est comptabilisé pour donner un score final.

Mode Correction : Une vue "solution" de la grille est affichée au tout début du jeu pour faciliter le test et la correction.

🛠️ Prérequis
Pour lancer ce jeu, vous avez seulement besoin de :

Python 3.x

🚀 Comment Jouer
Téléchargez le projet : Clonez ce dépôt ou téléchargez tous les fichiers .py dans un même dossier.

Ouvrez un terminal : Naviguez jusqu'au dossier où vous avez placé les fichiers.

Lancez le jeu avec la commande suivante : python main.py

Jouez !

La grille de la solution s'affichera une seule fois.

Ensuite, la grille du joueur apparaît.

Quand le jeu vous le demande (Entrez les coordonnées du tir (ex: 'x,y'):), entrez une colonne et une ligne (par exemple 3,5) et appuyez sur Entrée.

Le but est de couler tous les bateaux le plus rapidement possible !

📁 Structure du Projet
Le code est organisé en plusieurs fichiers pour une meilleure lisibilité :

main.py: Le cœur du jeu. Il contient la boucle principale, gère les tours du joueur et la logique de fin de partie.

grille.py: Définit la classe Grille, responsable de la gestion du plateau de jeu, de l'affichage et des tirs.

bateau.py: Contient la classe mère Bateau, qui définit les propriétés communes à tous les navires (longueur, position, orientation).

porte_avion.py: Classe fille pour le Porte-Avion.

croiseur.py: Classe fille pour le Croiseur.

torpilleur.py: Classe fille pour le Torpilleur.

sous_marin.py: Classe fille pour le Sous-Marin.

