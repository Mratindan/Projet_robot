#from Projet_robot.modele.Obstacle import Obstacle
from random import randint

import time

class Point:
    "Définition de la classe point"
    #Classe requise pour la classe Obstacle, permet d'indiquer la position du coin supérieur gauche d'un Obstacle
    def __init__(self,width,height):
        self.width = width
        self.height = height

class Obstacle:
    "Definition de la classe Obstacle"

    def __init__(self, abscisse, ordonnee,height,width):
        self.position = Point(abscisse, ordonnee)
        self.height = height
        self.width = width

    def __init__(self, abscisse, ordonnee):
        self.position = Point(abscisse, ordonnee)
        self.height = 0
        self.width = 0


class Roue:

    def __init__(self):
        self.moteurAllume=False
        self.vitesseRotation=0.

    def set_vitesse(self):
        return

class Arene(threading.Thread) :
    """
    Le modèle de l'arène, en attendant qu'il y ait les import nécessaires pour utiliser un objet arene ici. 
    """

    def __init__(self, width, height, robot, controleur):
        threading.Thread.__init__(self)
        self.width = width
        self.height = height
        self.robot = robot
        self.controleur = controleur
        self.list_obstacles = []

    def update(self):
        """
        Met à jour le modèle
        """
        self.robot.se_deplacer()
    
    def run(self):
        while True:
            #print(threading.current_thread)
            self.update()
            time.sleep(0.1)
            if self.controleur.done:
                break

    def initialiser_obstacles(self, n):
        """
        None -> None
        Crée et ajoute n obstacles avec une position aléatoire à la liste liste_obstacles. (Mettre des valeurs arbritaires pour la taille pour l'instant)
        """
        i = 0
        while(i < n):
            self.liste_obstacles.append(Obstacle(randint(0,self.width),randint(0,self.height),randint(5,10),randint(5,10)))
            i += 1

    def placer_obstacles(self, pos_largeur, pos_hauteur):
        """
        int * int
        Permet de placer un obstacle dans l'arène
        """
        print("La case est deja occupee, impossible de placer quoi que ce soit en ({},{})".format(posLargeur,
                                                                                                      posHauteur))
        self.terrain[posLargeur][posHauteur] = 'O'
        return

    def supprimerObstacle(self):
        """
        None -> None
        Permet de retirer le dernier obstacle de liste_obstacles
        """
        self.list_obstacles.pop()

    def update(self):

        """
        Met à jour la position du robot selon les instructions du controleur.
        """