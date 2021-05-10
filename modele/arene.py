import threading
import time
from .robot_simple import Robot_simple
from random import randint
from outils import Point, Vecteur

class Obstacle:
    """
    Definition de la classe Obstacle
    """

    def __init__(self, abscisse, ordonnee, height, width):
        self.x = abscisse
        self.y = ordonnee
        self.height = height
        self.width = width

class Arene(threading.Thread) :
    """
    Le modèle de l'arène.
    """

    def __init__(self, width, height, robot, controleur, nb_obstacles, lmax_obstacles):
        threading.Thread.__init__(self)
        self.width = width
        self.height = height
        self.robot = robot
        self.controleur = controleur
        self.liste_obstacles = []
        self.initialiser_obstacles(nb_obstacles, lmax_obstacles)

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
        if (self.robot.y < d) or (self.robot.y > (self.height - d)) or (self.robot.x < d) or (self.robot.x > (self.width - d)):
            self.robot.proche_obstacle = True
        else:
            self.robot.proche_obstacle = False

    def proximite_obstacles(self):
        """
        Met à jour l'état du robot en fonction de sa proximité avec les murs de l'arène.
        """
        for obstacle in self.liste_obstacles :
            d = self.robot.diametre_robot
            if (self.robot.y > (obstacle.height - d)) or (self.robot.x > (obstacle.width - d)):
                self.robot.proche_obstacle = True
            else:
                self.robot.proche_obstacle = False


    def initialiser_obstacles(self, n, lmax):
        """
        None -> None
        Crée et ajoute n obstacles avec une position aléatoire à la liste d'obstacles de l'arène.
        """
        for i in range(0, n):
            self.liste_obstacles.append(Obstacle(randint(0, self.width - 11), randint(0, self.height - 11), randint(5, lmax), randint(5, lmax)))

    def supprimerObstacle(self):
        """
        None -> None
        Permet de retirer le dernier obstacle de liste_obstacles
        """
        self.list_obstacles.pop()