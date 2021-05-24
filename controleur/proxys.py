import time

class Proxy_simu:
    def __init__(self, robot):
        self.robot = robot
        self.last_update = 0
        self.arene = None
    
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

    def proximite_obstacle(self):
        return self.arene.get_distance() <= 1
    
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
        self.last_action = 0
        self.vitesse_rg = 0
        self.vitesse_rd = 0
    
    def reset_time(self):
        self.robot.offset_motor_encode(self.robot.MOTOR_LEFT,self.robot.read_encoders()[0])
        self.robot.offset_motor_encode(self.robot.MOTOR_RIGHT,self.robot.read_encoders()[1])

    def avance_tout_droit(self, vitesse):
        """
        Action 1
        """
        self.last_action = 1
        self.robot.set_motor_dps(self, self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, vitesse)

    
    def tourne_droite(self, vitesse):
        """
        Action 2
        """
        self.last_action = 2
        self.robot.set_motor_dps(self, self.robot.MOTOR_LEFT, vitesse)
        self.robot.set_motor_dps(self, self.robot.MOTOR_LEFT, -vitesse)
    
    def tourne_gauche(self, vitesse):
        """
        Action 3
        """
        self.last_action = 3
        self.robot.set_motor_dps(self, self.robot.MOTOR_LEFT, -vitesse)
        self.robot.set_motor_dps(self, self.robot.MOTOR_LEFT, vitesse)

    def stop(self):
        self.robot.stop()

    def proximite_mur(self):
        return self.robot.get_distance() < 100

    def distance_parcourue(self, last_time):
        if self.last_action != 1 :
            raise Exception("distance_parcourue : la dernière action n'était pas avance_tout_droit")
        rg, rd = self.robot.get_motor_position()


    def angle_parcouru_droite(self, last_time):
        pass

    def angle_parcouru_gauche(self, last_time):
        pass