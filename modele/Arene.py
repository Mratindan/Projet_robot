from Projet_robot.modele.Obstacle import Obstacle

import time

class Arene:
    "Terrain sur lequel peut évoluer un robot et des objets quelconques"

    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.terrain = [[' '] * largeur for i in range(hauteur)]
        self.listeObstacles = []
        self.robot = None

    def placerObstacle(self, posLargeur, posHauteur):
        """
        int * int
        Permet de placer un obstacle dans l'arène
        """
        if Arene.estVide(posLargeur, posHauteur):
            self.listeObstacles.append(Obstacle())
            self.terrain[posLargeur][posHauteur] = 'O'
        else:
            print("La case est deja occupee, impossible de placer quoi que ce soit en ({},{})".format(posLargeur,
                                                                                                      posHauteur))
            self.terrain[posLargeur][posHauteur] = 'O'
            return

    def supprimerObstacle(self, posLargeur, posHauteur):
        """
        int * int
        Permet de retirer un obstacle present dans l'arène
        """
        if not (Arene.estVide(posLargeur, posHauteur)) and (Arene.terrain[posLargeur][posHauteur] == 'O'):
            self.terrain[posLargeur][posHauteur] = ' '
        else:
            print("La position donnee ({},{}) est deja vide.".format(posLargeur, posHauteur))
            return


# # Test rapide
# arene = Arene(30, 15)
# arene.afficherArene()
# print("Placons un obstacle en (10,10)")
# arene.placerObstacle(10, 10)
# arene.afficherArene()
# print("Essayons de placer un autre obstacle en (10,10)")
# arene.placerObstacle(10, 10)
# time.sleep(5)
#
# print("Supprimons maintenant l'obstacle que nous venons de creer")
# arene.supprimerObstacle(10, 10)
# arene.afficherArene()
# print("Essayons de le supprimer a nouveau")
# arene.supprimerObstacle(10, 10)
# arene.afficherArene()
#
# arene.estVide(31, 15)
# arene.estVide(2, 5)
# arene.estVide(10, 9)
#
# """if arene.estVide(1, 0):
#     print("La case est vide")
# else:
#     print("La case n'est pas vide")
#
#
# if arene.estVide(20, 30):
#     print("La case est vide")
# else:
#     print("La case n'est pas vide")"""
#

