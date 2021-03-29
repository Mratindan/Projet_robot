import threading
import time
import math
from abc import ABC, abstractmethod
from modele import Robot_simple


class Actions_elementaires(threading.Thread):
    """
    Cette classe contient toutes les actions élémentaires qui permettent de développer des stratégies.
    """

    def __init__(self, robot):
        threading.Thread.__init__(self)
        self.robot = robot 
        self.posx = 0
        self.posy = 0
        self.done = False

            
    def save_position(self):
        """
        Permet au controleur de se souvenir de la position actuelle du robot.
        """
        self.posx = self.robot.x
        self.posy = self.robot.y
        return 1


    def robot_stop(self):
        """
        Donne l'ordre au robot de s'arrêter.
        """
        self.robot.change_dir(0, 0)
        return 1
    

    def robot_avance(self, dx, dy):
        """
        Donne l'ordre au robot d'avancer dans une direction donnée par dx et dy.
        """
        self.robot.change_dir(dx, dy)
        return 1


    def parcourir(self, distance):
        """
        distance : int
        Permet de faire parcourir une distance donnée au robot en pixel dans une direction donnée par dx et dy.
        La fonction renvoie 1 si la distance voulue a bien été parcourue et -1 sinon.
        La distance effectivement parcourue est calculée à partir de la dernière position du robot enregistrée par le contrôleur.
        """
        distance_parcourue = math.sqrt((self.posx - self.robot.x)**2 + (self.posy - self.robot.y)**2)
        if (distance_parcourue < distance):
            return -1
        else :
            return 1    
    

    def update(self):
        pass
       

    def run(self):     
        while True:
            self.update()
            time.sleep(0.3)
            if self.done:
                break


class Controleur_carre(Actions_elementaires):
    """
    Cette classe définit la stratégie permettant de dessiner un carré.
    """

    def __init__(self, robot):
        Actions_elementaires.__init__(self, robot)
        self.save_position()
        print("La position du robot a été enregistrée par le controleur comme étant (", self.posx, ", ", self.posy, ")")
        self.robot_avance(1, 0)
        self.robot.crayon = True

    
    def update(self):
        if self.parcourir(20) == 1 :
            self.done = True
            self.robot_stop()
