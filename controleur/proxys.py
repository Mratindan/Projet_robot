import time
import math

class Proxy_simu:
    def __init__(self, robot):
        self.robot = robot
        self.last_update = 0

    def avance_tout_droit(self, vitesse):
        self.robot.set_vitesse(vitesse, vitesse)
    
    def tourne_droite(self, vitesse):
        self.robot.set_vitesse(vitesse, -vitesse)
    
    def tourne_gauche(self, vitesse):
        self.robot.set_vitesse(-vitesse, vitesse)
    
    def reset_time(self):
        self.last_update = time.time()

    def distance_parcourue(self, last_time):
        """
        Retourne la distance parcourue par le robot depuis la dernière mise à jour.
        """

        angle = (time.time() - last_time) * self.robot.v_roue_droite
        distance = (2 * math.pi * self.robot.diametre_roue/2 * angle) / 360
        return distance

    def angle_parcouru_droite(self, last_time):
        """
        Retourne l'angle parcouru vers la droite
        """
        angle = (time.time() - last_time) * self.robot.v_roue_gauche
        distance = (2 * math.pi * self.robot.diametre_roue/2 * angle) / 360
        angle = (360 * distance) / (2 * math.pi * self.robot.diametre_robot/2)

        return angle

    def angle_parcouru_gauche(self, last_time):
        """
        Retourne l'angle parcouru vers la gauche
        """
        angle = (time.time() - last_time) * self.robot.v_roue_droite
        distance = (2 * math.pi * self.robot.diametre_roue/2 * angle) / 360
        angle = (360 * distance) / (2 * math.pi * self.robot.diametre_robot/2)

        return angle
    
class Proxy_irl:
    def __init__(self, robot):
        self.robot = robot
        self.last_update = 0
    
    def reset_time(self):
        pass

    def avance_tout_droit(self, vitesse):
        pass
    
    def tourne_droite(self, vitesse):
        pass
    
    def tourne_gauche(self, vitesse):
        pass

    def distance_parcourue(self, last_time):
        pass

    def angle_parcouru_droite(self, last_time):
        pass

    def angle_parcouru_gauche(self, last_time):
        pass