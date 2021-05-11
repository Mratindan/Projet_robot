import threading
import time
from .robot_simple import Robot_simple
from random import randint
from outils import Point, Vecteur

class Obstacle:
    """
    Definition de la classe Obstacle
    """

    def __init__(self, posx, posy, width, height):
        self.x = posx
        self.y = posy
        self.width = width
        self.height = height


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
        #self.placer_obstacle(190, 200, 20, 15)
        self.initialiser_obstacles(nb_obstacles, lmax_obstacles)

    def update(self):
        """
        Met à jour le modèle
        """
        self.robot.se_deplacer()
        self.proximite_mur()
        self.proximite_obstacles()
    
    def run(self):
        while not (self.controleur.done()):
            self.update()
            time.sleep(0.01)

    def proximite_mur(self):
        """
        Met à jour l'état du robot en fonction de sa proximité avec les murs de l'arène.
        """
        d = self.robot.diametre_robot + self.robot.diametre_robot/2
        if (self.robot.y < d) or (self.robot.y > (self.height - d)) or (self.robot.x < d) or (self.robot.x > (self.width - d)):
            self.robot.proche_mur = True
        else:
            self.robot.proche_mur = False

    def proximite_obstacles(self):
        """
        Met à jour l'état du robot en fonction de sa proximité avec les obstacles de l'arène.
        """
        for obstacle in self.liste_obstacles :
            d = self.robot.diametre_robot + self.robot.diametre_robot/2
            if ((obstacle.y - d) < self.robot.y < (obstacle.y + obstacle.height + d)) and ((obstacle.x - d) < self.robot.x < (obstacle.x + obstacle.width + d)):
                self.robot.proche_obstacle = True
                break
            else:
                self.robot.proche_obstacle = False


    def initialiser_obstacles(self, n, lmax):
        """
        Crée et ajoute n obstacles avec une position aléatoire à la liste d'obstacles de l'arène.
        """
        for i in range(0, n):
            width =  randint(5, lmax)
            height = randint(5, lmax)
            self.liste_obstacles.append(Obstacle(randint(0, self.width - width), randint(0, self.height - height), width, height))

    def placer_obstacle(self, posx, posy, width, height):
        """
        Place un obstacle 
        """
        self.liste_obstacles.append(Obstacle(posx, posy, width, height))


    def supprimerObstacle(self):
        """
        None -> None
        Permet de retirer le dernier obstacle de liste_obstacles
        """
        self.list_obstacles.pop()