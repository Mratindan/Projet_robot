import time
import math

class Proxy_simu:
    def __init__(self, robot):
        self.robot = robot
        self.last_update = 0
    
    def reset_time(self):
        self.last_update = time.time()

    def avance_tout_droit(self, vitesse):
        self.robot.set_vitesse(vitesse, vitesse)
    
    def tourne_droite(self, vitesse):
        self.robot.set_vitesse(vitesse, -vitesse)
    
    def tourne_gauche(self, vitesse):
        self.robot.set_vitesse(-vitesse, vitesse)

    def stop(self):
        self.robot.set_vitesse(0, 0)

    def proximite_mur(self):
        return self.robot.proche_mur
    
    def distance_parcourue(self, last_time):
        """
        Retourne la distance parcourue par le robot depuis la dernière mise à jour.
        """
        return self.robot.distance_parcourue(self.last_update)

    def angle_parcouru_droite(self, last_time):
        """
        Retourne l'angle parcouru vers la droite
        """
        return self.robot.angle_parcouru_droite(self.last_update)

    def angle_parcouru_gauche(self, last_time):
        """
        Retourne l'angle parcouru vers la gauche
        """
        return self.robot.angle_parcouru_gauche(self.last_update)
    
class Proxy_irl:
    def __init__(self, robot):
        self.robot = robot
        self.last_update = 0
        self.last_position_robot = 0
    
    def reset_time(self):
        pass

    def avance_tout_droit(self, vitesse):
        self.robot.set_motor_dps(self, self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, vitesse)
    
    def tourne_droite(self, vitesse):
        self.robot.set_motor_dps(self, self.robot.MOTOR_LEFT, vitesse)
        self.robot.set_motor_dps(self, self.robot.MOTOR_LEFT, -vitesse)
    
    def tourne_gauche(self, vitesse):
        self.robot.set_motor_dps(self, self.robot.MOTOR_LEFT, -vitesse)
        self.robot.set_motor_dps(self, self.robot.MOTOR_LEFT, vitesse)

    def stop(self):
        self.robot.stop()

    def proximite_mur(self):
        pass

    def distance_parcourue(self, last_time):
        pass

    def angle_parcouru_droite(self, last_time):
        pass

    def angle_parcouru_gauche(self, last_time):
        pass