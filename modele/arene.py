import threading
import time
from .robot_simple import Robot_simple
from random import randint
from outils import Point, Vecteur
from controleur import Controleur_carre

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


class Roue:

    def __init__(self):
        self.moteurAllume=False
        self.vitesseRotation=0.

    def set_vitesse(self):
        return

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

    def supprimerObstacle(self):
        """
        None -> None
        Permet de retirer le dernier obstacle de liste_obstacles
        """
        self.list_obstacles.pop()