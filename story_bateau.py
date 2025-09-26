from bateau import Bateau


def chevauchent(b1: Bateau, b2: Bateau) -> bool:
    """Retourne True si les deux bateaux se chevauchent"""
    return any(pos in b2.positions for pos in b1.positions)


def main():
    b1 = Bateau(2, 3, longueur=3)  

    b2 = Bateau(2, 5, longueur=2)  

    if chevauchent(b1, b2):
        print("Les bateaux se chevauchent !")
    else:
        print("Les bateaux ne se chevauchent pas.")


if __name__ == "__main__":
    main()
