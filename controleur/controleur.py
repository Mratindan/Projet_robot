import threading
import time
import math
from modele import Robot_simple


class Controleur(threading.Thread):
    def __init__(self, action):
        threading.Thread.__init__(self)
        self.action = action

    def done(self):
        return self.action.done()

    def update(self):
        self.action.update()

    def demarre(self):
        self.action.demarre()

    def run(self): 
        self.demarre() 
        while not (self.done()):
            self.update()
            time.sleep(0.2)
            

class SequenceActions:
    def __init__(self,robot,liste):
        self.robot = robot
        self.liste = liste
        self.i = 0

    def done(self):
        return self.i >= len(self.liste)

    def update(self):
        if self.liste[self.i].done():
            self.i += 1
            if self.done(): 
                return None
            self.liste[self.i].demarre()
        self.liste[self.i].update()

    def demarre(self):
        self.i = 0
        self.liste[self.i].demarre()

class ParcourirAction:
    def __init__(self,robot,distance):
        self.robot = robot
        self.distance = distance
        self.vitesse = 3

    def done(self):
        distance_parcourue = self.robot.distance_parcourue(self.robot.last_update)
        return distance_parcourue > self.distance

    def update(self):
        if self.done(): 
            return None
        self.robot.avance_tout_droit(self.vitesse)
        

    def demarre(self):
        self.robot.reset_time()


class TournerDroiteAction:
    def __init__(self,robot,angle):
        self.robot = robot
        self.angle = angle
        self.vitesse = 10

    def done(self):
        angle_parcouru = self.robot.angle_parcouru_droite(self.robot.last_update)
        return angle_parcouru > self.angle

    def update(self):
        if self.done(): 
            return None
        self.robot.tourne_droite(self.vitesse)

    def demarre(self):
        self.robot.reset_time()


class TournerGaucheAction:
    def __init__(self,robot,angle):
        self.robot = robot
        self.angle = angle
        self.vitesse = 15

    def done(self):
        angle_parcouru = self.robot.angle_parcouru_gauche(self.robot.last_update)
        return angle_parcouru > self.angle

    def update(self):
        if self.done(): 
            return None
        self.robot.tourne_gauche(self.vitesse)

    def demarre(self):
        self.robot.reset_time()

class Robot2I013:
    def __init__(self,robot,distance):
        self.robot = robot
        self.distance = distance
        self.vitesse = 3
        
    def done(self):
        distance_parcourue = self.robot.distance_parcourue(self.robot.last_update)
        return distance_parcourue > self.distance
    
    def update(self):
        if self.done(): 
            if self.robot.crayon==True:
                self.robot.crayon=False
            else :
                self.robot.crayon=True
            return None
        self.robot.avance_tout_droit(self.vitesse)
        
    def demarre(self):
        self.robot.reset_time()

class Carre(SequenceActions):
    def __init__(self,robot):
        SequenceActions.__init__(self, robot, None)
        parcourir = ParcourirAction(robot, 0.2)
        tourner_droite = TournerDroiteAction(robot, 90)
        self.liste = [parcourir, tourner_droite] * 3 + [parcourir]

class Pointille(SequenceActions):
    def __init__(self,robot):
        SequenceActions.__init__(self, robot, None)
        parcourir = Robot2I013(robot, 0.5)
        self.liste = [parcourir] * 5
        
class Triangle(SequenceActions):
    def __init__(self,robot):
        SequenceActions.__init__(self, robot, None)
        parcourir = ParcourirAction(robot, 0.5)
        tourner_droite = TournerDroiteAction(robot, 120)
        self.liste = [parcourir, tourner_droite] * 3
    