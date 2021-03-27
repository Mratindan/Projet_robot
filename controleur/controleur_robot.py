import threading
import time
from abc import ABC, abstractmethod
from modele import Robot_simple

class Controleur_carre(threading.Thread):
    """
    La classe mère de tous les contrôleurs.
    """

    def __init__(self, robot):
        threading.Thread.__init__(self)
        self.robot = robot
        self.cpt = 0
        self.done = False 


    def update(self):
        self.tracer_carre()
        self.cpt += 1            


    def tracer_carre(self):
        """
        Pour faire "dessiner" un carré à un robot.
        """

        # Déplacement sur le côté haut (vers la droite)
        if (self.cpt < 20):
            self.robot.change_dir(1, 0)#on change la direction ici
            self.robot.crayon = True
            
        # Déplacement sur le côté droit (vers le bas)
        if (20 <= self.cpt) and (self.cpt < 40):
            self.robot.change_dir(0, 1)
            self.robot.crayon = True
        
        # Déplacement sur le côté bas (vers la gauche)
        if (40 <= self.cpt) and (self.cpt < 60):
            self.robot.change_dir(-1, 0)
            self.robot.crayon = True

        # Déplacement sur le côté gauche (vers le haut)
        if (60 <= self.cpt) and (self.cpt < 80):
            self.robot.change_dir(0, -1)
            self.robot.crayon = True

        if (self.cpt >= 80):
            self.robot.change_dir(0, 0)
            self.robot.crayon = False
            self.done = True


    def run(self):       
        while True:
            print("(Thread du controleur) cpt = ", self.cpt)
            self.update()
            time.sleep(0.3)
            if self.done:
                break
