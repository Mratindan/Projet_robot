import threading
import time
import math

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
    def __init__(self, liste):
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
    def __init__(self, proxy, distance):
        self.proxy = proxy
        self.distance = distance
        self.vitesse = 3

    def done(self):
        distance_parcourue = self.proxy.distance_parcourue(self.proxy.last_update)
        return distance_parcourue > self.distance

    def update(self):
        if self.done(): 
            return None
        self.proxy.avance_tout_droit(self.vitesse)
        

    def demarre(self):
        self.proxy.reset_time()


class TournerDroiteAction:
    def __init__(self, proxy, angle):
        self.proxy = proxy
        self.angle = angle
        self.vitesse = 10

    def done(self):
        angle_parcouru = self.proxy.angle_parcouru_droite(self.proxy.last_update)
        return angle_parcouru > self.angle

    def update(self):
        if self.done(): 
            return None
        self.proxy.tourne_droite(self.vitesse)

    def demarre(self):
        self.proxy.reset_time()


class TournerGaucheAction:
    def __init__(self, proxy, angle):
        self.proxy = proxy
        self.angle = angle
        self.vitesse = 15

    def done(self):
        angle_parcouru = self.proxy.angle_parcouru_gauche(self.proxy.last_update)
        return angle_parcouru > self.angle

    def update(self):
        if self.done(): 
            return None
        self.proxy.tourne_gauche(self.vitesse)

    def demarre(self):
        self.proxy.reset_time()


class Carre(SequenceActions):
    def __init__(self, proxy):
        SequenceActions.__init__(self, None)
        parcourir = ParcourirAction(proxy, 0.2)
        tourner_droite = TournerDroiteAction(proxy, 90)
        self.liste = [parcourir, tourner_droite] * 3 + [parcourir]