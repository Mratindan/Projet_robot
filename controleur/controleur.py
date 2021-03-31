import threading
import time
import math
from modele import Robot_simple


class Controleur(Threading.thread):
    def __init__(self,robot,action):
        self.action = action
        self.robot = robot

    def done(self):
        return self.action.done()
    def next(self):
        self.action.next()
    def start(self):
        self.action.start()
    def run(self):  
        self.start()   
        while not self.done():
            self.next()
            time.sleep(0.2)
            

class SequenceActions:
    def __init__(self,robot,liste):
        self.liste = liste
        self.i = 0

    def done(self):
        return self.i >= len(self.liste)
    def update(self):
        if self.liste[self.i].done():
            self.i += 1
            if self.done(): return None
            self.liste[i].start()
        self.liste[i].update()
    def start(self):
        self.i = 0
        self.liste[self.i].start()

class ParcourirAction:
    def __init__(self,robot,distance):
        self.robot = robot
        self.distance = distance
        self.vitesse = 1
    def done(self):
        distance_parcourue = self.robot.distance_parcourue()
        return distance_parcourue > self.distance
    def update(self):
        if self.done(): return
        self.robot.avance_tout_droit()
    def start(self):
        self.robot.reset_time()
        self.posx, self.posy = self.robot.x, self.robot.y


class TournerGaucheAction:
    def __init__(self,robot,angle):
        self.angle = angle
        self.vitesse = 50
    def done(self):
        nouvel_angle = math.sqrt((self.posx - self.robot.x)**2 + (self.posy - self.robot.y)**2)
        return angle > nouvel_angle
    def update(self):
        if self.done(): return
        self.robot.change_dir(0,self.vitesse)
    def start(self):
        self.posx,self.posy = self.robot.x,self.robot.y

        
class Carre(SequenceActions):
    def __init__(self,robot):
        SequenceActions.__init__(robot, None)
        parcourir = ParcourirAction(robot,10)
        tourner = TournerGaucheAction(robot,90)
        self.liste = [parcourir,tourner]*4