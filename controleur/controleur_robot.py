import modele
import threading
import time
from abc import ABC, abstractmethod
from modele import Robot_simple

class Actions_elementaires(threading.Thread, ABC):
    """
    La classe mère de tous les contrôleurs. (Ne pas oublier les import lors de la copie dans un autre fichier)
    """

    def __init__(self, robot):
        threading.Thread.__init__(self)
        self.robot = robot
        self.cpt = 0
        self.done = False 


    @abstractmethod
    def update(self):
        pass           


    def run(self):     
        while True:
            #print(threading.current_thread)
            self.update()
            time.sleep(0.3)
            if self.done:
                break
    

    def aller_tout_droit(self, distance):
        self.robot.se_deplacer()
    

    def tourner_angle_droit(self):
        """
        Permet de donner l'ordre au robot de tourner à 90° dans le sens des aiguilles d'une montre.
        """
        


class Controleur_carre(Actions_elementaires) :
    """Le controleur qui permet au robot de faire un carré, en attendant qu'il y ait les import nécessaires pour utiliser les fichiers du module controleur ici."""

    def __init__(self, robot):
        Controleur_robot.__init__(self, robot)


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
