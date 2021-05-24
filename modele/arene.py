import threading
import time
import math
from random import randint

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
        self.robot_dirx = self.robot.x
        self.robot_diry = self.robot.y

    def update(self):
        """
        Met à jour le modèle
        """
        self.robot.se_deplacer()
        self.get_distance()
        #print("ANGLE ROBOT : ", self.robot.angle)
        
    def run(self):
        while not (self.controleur.done()):
            self.update()
            time.sleep(0.01)


    def est_exterieur_mur(self, x, y):
        """
        Renvoie True si le point de coordonnées (x, y) se trouve à l'extérieur des bords de l'arène et False sinon.
        """
        if (x < 0) or (x > self.width) or (y < 0) or (y > self.height):
            return True
        else:
            return False

    def est_interieur_obstacles(self, x, y):
        """
        Renvoie True si le point de coordonnées (x, y) se trouve à l'intérieur d'un obstacle de l'arène et False sinon.
        """
        for obstacle in self.liste_obstacles :
            if (obstacle.x <= x <= obstacle.x + obstacle.width) and (obstacle.y <= y <= obstacle.y + obstacle.height):
                return True

        return False

    def get_distance(self):
        """
        Retourne la distance du premier obstacle dans la direction du robot en nombre de pas avec un pas = self.robot.diametre_robot + self.robot.diametre_robot/2
        """
        d = self.robot.diametre_robot + self.robot.diametre_robot/2
        # Direction
        dir = math.radians(self.robot.angle)
        # Point se trouvant à une distance d de la position du robot dans cette direction
        x0 = self.robot.x
        y0 = self.robot.y
        x1 = x0
        y1 = y0
        pas = 0

        while not (self.est_exterieur_mur(x1, y1) or self.est_interieur_obstacles(x1, y1)):
            x1 = x0 + d * math.cos(dir)
            y1 = y0 + d * math.sin(dir)
            self.robot_dirx = x1
            self.robot_diry = y1
            #print("get_distance itération", pas, " : ", self.robot_dirx, self.robot_diry)
            x0 = x1
            y0 = y1
            pas += 1

        return pas

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