# coding: utf-8
import time
import math


class Robot_simple :
    def __init__(self, x, y):
        """ 
        Représente un robot avec une position initiale (x, y) 
        """
        self.x = x
        self.y = y
        self.angle = 0 # La direction dans laquelle pointe la tête du robot
        self.v_roue_gauche = 0
        self.v_roue_droite = 0
        self.diametre_roue = 5 # 66.5
        self.diametre_robot = 10 # 117
        self.last_update = 0
        self.last_se_deplacer = 0
        self.crayon = True # Définit si le robot utilise un crayon ou pas
        self.echelle = 100 # 1 metre pour le robot IRL = 100 pixel dans la simulation
        self.signal = 0

    def get_signal(self):
        return signal

    def set_vitesse(self, v_roue_g, v_roue_d):
        self.v_roue_gauche = v_roue_g
        self.v_roue_droite = v_roue_d
    
    def avance_tout_droit(self, vitesse):
        """
        Pour le proxy
        """
        self.set_vitesse(vitesse, vitesse)
    
    def tourne_droite(self, vitesse):
        """
        Pour le proxy
        """
        self.set_vitesse(vitesse, -vitesse)
    
    def tourne_gauche(self, vitesse):
        """
        Pour le proxy
        """
        self.set_vitesse(-vitesse, vitesse)
    
    def reset_time(self):
        self.last_update = time.time()
    
    def reset_se_deplacer_time(self):
        self.last_se_deplacer = time.time()

    def distance_parcourue(self, last_time):
        """
        Retourne la distance parcourue par le robot depuis la dernière mise à jour.
        """

        angle = (time.time() - last_time) * self.v_roue_droite
        distance = (2 * math.pi * self.diametre_roue/2 * angle) / 360
        return distance

    def angle_parcouru_droite(self, last_time):
        """
        Retourne l'angle parcouru vers la droite
        """
        angle = (time.time() - last_time) * self.v_roue_gauche
        distance = (2 * math.pi * self.diametre_roue/2 * angle) / 360
        angle = (360 * distance) / (2 * math.pi * self.diametre_robot/2)

        return angle

    def angle_parcouru_gauche(self, last_time):
        """
        Retourne l'angle parcouru vers la gauche
        """
        angle = (time.time() - last_time) * self.v_roue_droite
        distance = (2 * math.pi * self.diametre_roue/2 * angle) / 360
        angle = (360 * distance) / (2 * math.pi * self.diametre_robot/2)

        return angle

    
    def se_deplacer(self):
        """
        Permet de simuler le déplacement du robot à partir de sa vitesse
        """

        if (self.last_se_deplacer == 0):
            self.reset_se_deplacer_time()

        # si le robot avance tout droit
        if (self.v_roue_droite == self.v_roue_gauche):
            distance = self.distance_parcourue(self.last_se_deplacer)
            self.x += distance * math.cos(math.radians(self.angle - 90)) * self.echelle
            self.y += distance * math.sin(math.radians(self.angle - 90)) * self.echelle 
            self.reset_se_deplacer_time()

            return None
            
        # si le robot tourne sur lui-même
        elif (-self.v_roue_droite == self.v_roue_gauche):
            # si le robot tourne sur lui-même vers la droite
            if (self.v_roue_droite < 0): 
                self.angle += self.angle_parcouru_droite(self.last_se_deplacer)
                self.reset_se_deplacer_time()
                return None
            # si le robot tourne sur lui-même vers la gauche
            else :
                self.angle -= self.angle_parcouru_gauche(self.last_se_deplacer)
                self.reset_se_deplacer_time()
                return None
        
        raise Exception()
        