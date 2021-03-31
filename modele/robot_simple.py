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
        self.width = 10
        self.height = 10
        self.v_roue_gauche = 0
        self.v_roue_droite = 0
        self.diametre_roue = 0 # 66.5
        self.diametre_robot = 0 # 117
        self.last_update = time.localtime()
        self.last_se_deplacer = 0
        self.crayon = False # Définit si le robot utilise un crayon ou pas
    
    def set_vitesse(self, v_roue_g, v_roue_d):
        self.v_roue_gauche = v_roue_g
        self.v_roue_droite = v_roue_d
    
    def avance_tout_droit(self, vitesse):
        """
        Pour le proxy
        """
        self.set_vitesse(vitesse, vitesse)
    
    def tourner_droite(self, vitesse):
        """
        Pour le proxy
        """
        self.set_vitesse(vitesse, -vitesse)
    
    def tourner_gauche(self, vitesse):
        """
        Pour le proxy
        """
        self.set_vitesse(-vitesse, vitesse)

    def distance_parcourue(self, last_time):
        """
        Retourne la distance parcourue par le robot depuis la dernière mise à jour.
        """
        angle = (time.localtime() - last_time) * self.v_roue_droite
        distance = (2 * math.pi * diametre_roue/2 * angle) / 360
        return distance

    def reset_time(self):
        self.last_update = time.localtime()

    def angle_parcouru(self, last_time):
        """
        Retourne l'angle parcouru
        """
        angle = (time.localtime - self.last_time) * self.v_roue_droite
        distance = (2 * math.pi * diametre_roue/2 * angle) / 360
        angle = (360 * distance) / (2 * math.pi * diametre_robot/2)

        return angle

    
    def se_deplacer(self):
        """
        Permet au robot de se déplacer
        """
        # si le robot tourne sur lui-même
        if (-self.v_roue_droite == self.v_roue_gauche):
            # si le robot tourne sur lui-même vers la droite
            if (self.v_roue_droite < 0): 
                self.angle += self.angle_parcouru(self.last_se_deplacer)
                return None
            # si le robot tourne sur lui-même vers la gauche
            else :
                self.angle -= self.angle_parcouru(self.last_se_deplacer)
                return None
            
        # si le robot avance tout droit
        if (self.v_roue_droite == self.v_roue_gauche):
            distance = self.distance_parcourue(self.last_se_deplacer)
            self.x += distance * math.cos() * self.angle
            self.y += distance * math.sin() * self.angle

            return None
        
        raise Exception()
        