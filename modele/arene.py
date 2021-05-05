import threading
import time
from .robot_simple import Robot_simple
from random import randint
from outils import Point, Vecteur

class Obstacle:
    """
    Definition de la classe Obstacle
    """

    def __init__(self, abscisse, ordonnee,height,width):
        self.position = Point(abscisse, ordonnee)
        self.height = height
        self.width = width

    def __init__(self, abscisse, ordonnee):
        self.position = Point(abscisse, ordonnee)
        self.height = 0
        self.width = 0


class Arene(threading.Thread) :
    """
    Le modèle de l'arène.
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
        self.proximite_mur()
    
    def run(self):
        while not (self.controleur.done()):
            self.update()
            time.sleep(0.1)

    def proximite_mur(self):
        """
        Met à jour l'état du robot en fonction de sa proximité avec les murs de l'arène.
        """
        d = self.robot.diametre_robot
        if (self.robot.y < d) or (self.robot.y > (self.height - d)) or (self.robot.x < d) or (self.robot.x > (self.width - d)) :
            self.robot.proche_mur = True
        else :
            self.robot.proche_mur = False

    def initialiser_obstacles(self, n):
        """
        None -> None
        Crée et ajoute n obstacles avec une position aléatoire à la liste liste_obstacles. (Mettre des valeurs arbritaires pour la taille pour l'instant)
        """
        i = 0
        while(i < n):
            self.liste_obstacles.append(Obstacle(randint(0,self.width),randint(0,self.height),randint(5,10),randint(5,10)))
            i += 1

    def supprimerObstacle(self):
        """
        None -> None
        Permet de retirer le dernier obstacle de liste_obstacles
        """
        self.list_obstacles.pop()