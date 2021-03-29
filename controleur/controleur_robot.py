import threading
import time
import math
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
        self.liste = []
        self.len_liste = 0
        self.i = 0
        self.done = False

            
    def save_position(self):
        """
        Permet au controleur de se souvenir de la position actuelle du robot.
        """
        self.posx = self.robot.x
        self.posy = self.robot.y
        print("La position du robot a été enregistrée par le contrôleur comme étant (", self.posx, ", ", self.posy, ")")
        return 1


    def robot_avance(self, dx, dy):
        """
        Donne l'ordre au robot d'avancer dans une direction donnée par dx et dy.
        """
        self.robot.change_dir(dx, dy)
        return 1


    def robot_stop(self):
        """
        Donne l'ordre au robot de s'arrêter.
        """
        self.robot.change_dir(0, 0)
        return 1
    

    def robot_dessine(self):
        self.robot.crayon = True
        return 1
    

    def robot_dessine_stop(self):
        self.robot.crayon = False
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
        
    
    def next(self):
        if (self.i < self.len_liste) and (self.liste[self.i]() == 1):
            if (self.i == self.len_liste - 1):
                self.done = True
            else :
                self.i += 1
    

    def update(self):
        self.done = True
       

    def run(self):     
        while True:
            self.update()
            time.sleep(0.2)
            if self.done:
                break


class Controleur_carre(Actions_elementaires):
    """
    Cette classe définit la stratégie permettant de dessiner un carré.
    """

    def __init__(self, robot):
        Actions_elementaires.__init__(self, robot)
        self.liste = [
            lambda : self.robot_dessine(),
            lambda : self.save_position(),  
            lambda : self.robot_avance(1, 0),
            lambda : self.parcourir(20),
            lambda : self.save_position(),  
            lambda : self.robot_avance(0, 1),
            lambda : self.parcourir(20),
            lambda : self.save_position(),  
            lambda : self.robot_avance(-1, 0),
            lambda : self.parcourir(20),
            lambda : self.save_position(),  
            lambda : self.robot_avance(0, -1),
            lambda : self.parcourir(20),
            lambda : self.robot_stop(),
            lambda : self.robot_dessine_stop()
        ]
        self.len_liste = len(self.liste)
        

    def update(self):
        self.next()
