import threading
import time
import random

class Controleur(threading.Thread):
    def __init__(self, proxy, action):
        threading.Thread.__init__(self)
        self.action = action
        self.proxy = proxy

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
            time.sleep(0.1)


class ConditionActions:
    def __init__(self, proxy, action_principale, action_alternative, condition):
        self.action_principale = action_principale
        self.action_alternative = action_alternative
        self.condition = condition
        self.proxy = proxy
        self.est_en_cours = False

    def done(self):
        return self.action_principale.done() or self.action_alternative.done()

    def update(self):
        if self.done(): 
            self.action_principale.est_en_cours = False
            self.action_alternative.est_en_cours = False
            return None
        if self.condition(self.proxy):
            if not self.action_alternative.est_en_cours:
                self.action_alternative.demarre()
            self.action_alternative.update()
        else : 
            self.action_principale.update()

    def demarre(self):
        self.action_principale.demarre()
        self.est_en_cours = True

class BoucleAction:
    def __init__(self, proxy, loop_action):
        self.loop_action = loop_action
        self.proxy = proxy
        self.est_en_cours = False

    def done(self):
        return False

    def update(self):
        if self.done(): 
            return None
        if self.loop_action.done():
            self.loop_action.demarre()
        else:
            self.loop_action.update()

    def demarre(self):
        self.loop_action.demarre()
        self.est_en_cours = True
            
class SequenceActions:
    def __init__(self, proxy, liste):
        self.liste = liste
        self.i = 0
        self.proxy = proxy
        self.est_en_cours = False

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
        self.est_en_cours = True


class ParcourirAction:
    def __init__(self, proxy, distance, vitesse):
        self.proxy = proxy
        self.distance = distance
        self.vitesse = vitesse
        self.est_en_cours = False

    def done(self):
        distance_parcourue = self.proxy.distance_parcourue(self.proxy.last_update)
        print("Distance parcourue :", distance_parcourue)
        return distance_parcourue > self.distance

    def update(self):
        if self.done(): 
            return None
        self.proxy.avance_tout_droit(self.vitesse)
        
    def demarre(self):
        self.proxy.reset_time()
        self.est_en_cours = True


class TournerDroiteAction:
    def __init__(self, proxy, angle, vitesse):
        self.proxy = proxy
        self.angle = angle
        self.vitesse = vitesse
        self.est_en_cours = False

    def done(self):
        angle_parcouru = self.proxy.angle_parcouru_droite(self.proxy.last_update)
        print("Angle parcouru : ", angle_parcouru)
        return angle_parcouru > self.angle

    def update(self):
        if self.done(): 
            return None
        self.proxy.tourne_droite(self.vitesse)

    def demarre(self):
        self.proxy.reset_time()
        self.est_en_cours = True


class TournerGaucheAction:
    def __init__(self, proxy, angle, vitesse):
        self.proxy = proxy
        self.angle = angle
        self.vitesse = vitesse
        self.est_en_cours = False

    def done(self):
        angle_parcouru = self.proxy.angle_parcouru_gauche(self.proxy.last_update)
        return angle_parcouru > self.angle

    def update(self):
        if self.done(): 
            return None
        self.proxy.tourne_gauche(self.vitesse)

    def demarre(self):
        self.proxy.reset_time()
        self.est_en_cours = True

class StopAction:
    def __init__(self, proxy):
        self.proxy = proxy
        self.est_en_cours = False

    def done(self):
        return self.est_en_cours
    
    def update(self):
        if self.done():
            return None
    
    def demarre(self):
        self.proxy.stop()
        self.est_en_cours = True

class TournerAction(SequenceActions):
    def __init__(self, proxy, angle, vitesse):
        super().__init__(proxy, None)
        if (angle >= 0):
            tourne = TournerDroiteAction(proxy, angle, vitesse)
        else:
            while (angle < 0):
                angle += 360
            tourne = TournerGaucheAction(proxy, 360 - angle, vitesse)
        self.liste = [tourne]

class BoucleSurTourne(BoucleAction):
    def __init__(self, proxy, vitesse):
        super().__init__(proxy, None)
        self.loop_action = TournerAction(proxy, 1, vitesse)

class AvanceJusquAuMur(ConditionActions):
    def __init__(self, proxy, vitesse):
        super().__init__(proxy, ParcourirAction(proxy, 1000, vitesse), StopAction(proxy), test_proximite_obstacle)

class NouvelleDirectionAction(ConditionActions):
    def __init__(self, proxy, vitesse_rotation):
        super().__init__(proxy, BoucleSurTourne(proxy, vitesse_rotation), StopAction(proxy), test_non_proximite_obstacle)

class Carre(SequenceActions):
    def __init__(self, proxy, longueur_cote, vitesse_deplacement, vitesse_rotation):
        super().__init__(proxy, None)
        parcourir = ParcourirAction(proxy, longueur_cote, vitesse_deplacement)
        tourner_droite = TournerDroiteAction(proxy, 90, vitesse_rotation)
        self.liste = [parcourir, tourner_droite] * 3 + [parcourir]

class TourneAvanceStop(SequenceActions):
    def __init__(self, proxy, angle, vitesse):
        super().__init__(proxy, None)
        tourne = TournerDroiteAction(proxy, angle, vitesse)
        avance_stop = AvanceJusquAuMur(proxy, vitesse)
        self.liste = [tourne, avance_stop]

class AvanceJusquAuMurPuisNouvelleDirection(SequenceActions):
    def __init__(self, proxy, vitesse_deplacement, vitesse_rotation):
        super().__init__(proxy, None)
        avance_stop = AvanceJusquAuMur(proxy, vitesse_deplacement)
        nouvelle_dir = NouvelleDirectionAction(proxy, vitesse_rotation)
        self.liste = [avance_stop, nouvelle_dir]

class ParcoursAutonome(SequenceActions):
    def __init__(self, proxy, vitesse_deplacement, vitesse_rotation):
        super().__init__(proxy, None)
        self.vd = vitesse_deplacement
        self.vr = vitesse_rotation
        avance_stop = AvanceJusquAuMur(proxy, self.vd)
        nouvelle_dir = NouvelleDirectionAction(self.proxy,self.vr)
        self.liste = [avance_stop, nouvelle_dir]

    def update(self):
        if self.liste[self.i].done():
            self.i += 1
            if self.done(): 
                avance_stop = AvanceJusquAuMur(self.proxy, self.vd)
                nouvelle_dir = NouvelleDirectionAction(self.proxy, self.vr)
                self.i = 0
                self.liste[0] = avance_stop
                self.liste[1] = nouvelle_dir
            self.liste[self.i].demarre()
        self.liste[self.i].update()

def test_proximite_obstacle(proxy):
    return proxy.proximite_obstacle()

def test_non_proximite_obstacle(proxy):
    return not proxy.proximite_obstacle()