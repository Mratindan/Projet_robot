# -*- coding: utf-8 -*-
import time
import math

class Robot_simple :
    def __init__(self, x, y):
        """ 
        Représente un robot avec une position initiale (x, y) 
        """
        self.x = x
        self.y = y
        self.angle = 0 # La direction de la tête du robot
        self.v_roue_gauche = 0
        self.v_roue_droite = 0
        self.diametre_roue = 7 # 66.5
        self.diametre_robot = 15 # 117
        self.last_update = 0
        self.crayon = True # Définit si le robot utilise un crayon ou pas
        self.echelle = 100 # 1 metre pour le robot IRL = 100 unités dans la simulation
    def set_v_roue_gauche(self,v):
        self.v_roue_gauche = v

    def set_v_roue_droite(self,v):
        self.v_roue_droite = v

    def set_vitesse(self, v_roue_g, v_roue_d):
        self.v_roue_gauche = v_roue_g
        self.v_roue_droite = v_roue_d
    
    def reset_time(self):
        self.last_update = time.time()

    def distance_parcourue(self, last_time):
        """
        Retourne la distance parcourue par le robot depuis la dernière mise à jour.
        """

        angle = (time.time() - last_time) * self.v_roue_droite
        distance = (math.pi * self.diametre_roue * angle) / 360

        return distance

    def angle_parcouru_droite(self, last_time):
        """
        Retourne l'angle parcouru vers la droite
        """
        angle = (time.time() - last_time) * self.v_roue_gauche
        distance = (math.pi * self.diametre_roue * angle) / 360
        angle_parcouru = (360 * distance) / (math.pi * self.diametre_robot)

        return angle_parcouru

    def angle_parcouru_gauche(self, last_time):
        """
        Retourne l'angle parcouru vers la gauche
        """
        angle = (time.time() - last_time) * self.v_roue_droite
        distance = (math.pi * self.diametre_roue * angle) / 360
        angle_parcouru = (360 * distance) / (math.pi * self.diametre_robot)

        return angle_parcouru

    def se_deplacer(self):
        """
        Permet de simuler le déplacement du robot.
        """

        if (self.last_update == 0):
            self.reset_time()

        # si le robot avance tout droit
        if (self.v_roue_droite == self.v_roue_gauche):
            distance = self.distance_parcourue(self.last_update)
            self.x += distance * math.cos(math.radians(self.angle)) * self.echelle
            self.y += distance * math.sin(math.radians(self.angle)) * self.echelle 
            self.reset_time()

            return None
            
        # si le robot tourne sur lui-même
        elif (-self.v_roue_droite == self.v_roue_gauche):
            # si le robot tourne sur lui-même vers la droite
            if (self.v_roue_droite < 0): 
                self.angle += self.angle_parcouru_droite(self.last_update)
                self.reset_time()
                return None
            # si le robot tourne sur lui-même vers la gauche
            else :
                self.angle -= self.angle_parcouru_gauche(self.last_update)
                self.reset_time()
                return None
        
        raise Exception()
        