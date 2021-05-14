import threading
import time
import math
from modele import Robot, Robot_simple, Polynome
from outils import Point, Vecteur


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


class Carre(SequenceActions):
    def __init__(self,robot):
        SequenceActions.__init__(self, robot, None)
        parcourir = ParcourirAction(robot, 0.2)
        tourner_droite = TournerDroiteAction(robot, 90)
        self.liste = [parcourir, tourner_droite] * 3 + [parcourir]
        
class Trajectoire:
    def __init__(self,robot,duree,acc,ang):
        self.robot=robot
        self.duree=duree
        self.acc=acc
        self.ang=ang

    def done(self):
        somme=time.time()-self.robot.last_update
        return somme>=self.duree
    
    def update(self):
        if self.done(): 
            return None
        
    def demarre(self):
        self.robot.changePosition(self.acc,self.ang)
        self.robot.reset_time()
        
class TrajectoireVitesse:
    def __init__(self,robot,vitesse,acc,ang):
        self.robot=robot
        self.vitesse=vitesse
        self.vitesseIni=0
        self.acc=acc
        self.ang=ang
        
    def done(self):
        if self.vitesse>=self.vitesseIni:
            return self.robot.vitesse>=self.vitesse
        if self.vitesse<self.vitesseIni:
            return self.robot.vitesse<self.vitesse
    
    def update(self):
        if self.done():
            return None
        
    def demarre(self):
        self.vitesseIni=self.robot.vitesse
        self.robot.changePosition(self.acc,self.ang)
        self.robot.reset_time()
        
class TrajectoireDistance:
    def __init__(self,robot,distance,acc,ang):
        self.robot=robot
        self.distance=distance
        self.acc=acc
        self.ang=ang
        
    def done(self):
        return self.robot.distance>=self.distance
    
    def update(self):
        if self.done():
            return None
        self.robot.distance_parcourue()
        
    def demarre(self):
        self.robot.distance=0
        self.robot.changePosition(self.acc,self.ang)
        self.robot.reset_time()

class Stop:
    def __init__(self,robot,acc,ang):
        self.robot=robot
        self.acc=acc
        self.ang=ang
        
    def done(self):
        return self.robot.vitesse<math.sqrt(pow(self.robot.vitesseVecteur.point1.calcul(time.time()-self.robot.last_update+0.1),2)+pow(self.robot.vitesseVecteur.point2.calcul(time.time()-self.robot.last_update+0.1),2))
    
    def update(self):
        if self.done():
            return None
        
    def demarre(self):
        if self.acc>0:
            self.acc=-self.acc
        self.robot.changePosition(self.acc,self.ang)
        self.robot.reset_time()
        
class Reset_vitesse:
    def __init__(self,robot):
        self.robot=robot
        
    def done(self):
        return True
    
    def update(self):
        if self.done():
            return None
        
    def demarre(self):
        self.robot.vitesseVecteur=Vecteur(Polynome(0,0,0),Polynome(0,0,0))
        
class Tourner(SequenceActions):
    def __init__(self,robot,vitesse,angle):
        SequenceActions.__init__(self, robot, None)
        trajec=TrajectoireVitesse(robot,vitesse/10,-vitesse/2,0)
        trajec2=Trajectoire(robot,1,vitesse*3,angle)
        trajec3=Trajectoire(robot,0.5,-vitesse*3,0)
        trajec4=TrajectoireVitesse(robot,vitesse,-vitesse/4,0)
        self.liste=[trajec]+[trajec2]+[trajec3]+[trajec4]
        
class Carre2(SequenceActions):
    def __init__(self,robot):
        SequenceActions.__init__(self, robot, None)
        trajec=Trajectoire(robot,1,150,0)
        trajec2=Trajectoire(robot,0.5,-150,0)
        trajec3=TrajectoireVitesse(robot,45,-12.5,0)
        trajec4=Tourner(robot,50,90)
        trajec5=Tourner(robot,50,90)
        trajec6=Tourner(robot,50,90)
        trajec7=TrajectoireVitesse(robot,5,-25,0)
        self.liste=[trajec]+[trajec2]+[trajec3]+[trajec4]+[trajec5]+[trajec6]+[trajec7]
        
class Test(SequenceActions):
    def __init__(self,robot):
        SequenceActions.__init__(self, robot, None)
        trajec=Trajectoire(robot,3,10,0)
        trajec2=Trajectoire(robot,2,100,90)
        trajec3=Trajectoire(robot,1,1000,90)
        self.liste=[trajec]+[trajec2]+[trajec3]
        
class Test2(SequenceActions):
    def __init__(self,robot):
        SequenceActions.__init__(self, robot, None)
        trajec=TrajectoireVitesse(robot,50,10,0)
        trajec2=TrajectoireVitesse(robot,1,-10,0)
        self.liste=[trajec]+[trajec2]
        
class Test3(SequenceActions):
    def __init__(self,robot):
        SequenceActions.__init__(self, robot, None)
        trajec=TrajectoireDistance(robot,100,10,0)
        trajec2=TrajectoireDistance(robot,100,-50,0)
        self.liste=[trajec]+[trajec2]
        
class Test4(SequenceActions):
    def __init__(self,robot):
        SequenceActions.__init__(self, robot, None)
        trajec=Trajectoire(robot,3,10,0)
        trajec2=Stop(robot,-50,0)
        trajec3=Reset_vitesse(robot)
        trajec4=Trajectoire(robot,5,10,-90)
        self.liste=[trajec]+[trajec2]+[trajec3]+[trajec4]
        