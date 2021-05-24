import threading
import time

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
            

class SequenceActions:
    def __init__(self, proxy, liste):
        self.liste = liste
        self.i = 0
        self.proxy = proxy

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


class ConditionActions:
    def __init__(self, proxy, action_principale, action_alternative, condition):
        self.action_principale = action_principale
        self.action_alternative = action_alternative
        self.condition = condition
        self.proxy = proxy

    def done(self):
        return self.action_principale.done() or self.action_alternative.done()

    def update(self):
        if self.done(): 
            return None
        if self.condition(self.proxy):
            if not self.action_alternative.est_en_cours:
                self.action_alternative.demarre()
            self.action_alternative.update()
        else : 
            self.action_principale.update()

    def demarre(self):
        self.action_principale.demarre()


class ParcourirAction:
    def __init__(self, proxy, distance, vitesse):
        self.proxy = proxy
        self.distance = distance
        self.vitesse = vitesse
        self.est_en_cours = False

    def done(self):
        distance_parcourue = self.proxy.distance_parcourue(self.proxy.last_update)
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
        SequenceActions.__init__(self, proxy, None)
        if (angle >= 0):
            tourne = TournerDroiteAction(proxy, angle, vitesse)
        else:
            while (angle < 0):
                angle += 360
            tourne = TournerGaucheAction(proxy, 360 - angle, vitesse)
        self.liste = [tourne]

class AvanceJusquAuMur(ConditionActions):
    def __init__(self, proxy, vitesse):
        ConditionActions.__init__(self, proxy, ParcourirAction(proxy, 1000, vitesse), StopAction(proxy), test_proximite_mur)

class Carre(SequenceActions):
    def __init__(self, proxy, longueur_cote, vitesse_deplacement, vitesse_rotation):
        SequenceActions.__init__(self, proxy, None)
        parcourir = ParcourirAction(proxy, longueur_cote, vitesse_deplacement)
        tourner_droite = TournerDroiteAction(proxy, 90, vitesse_rotation)
        self.liste = [parcourir, tourner_droite] * 3 + [parcourir]

class TourneAvanceStop(SequenceActions):
    def __init__(self, proxy, angle, vitesse):
        SequenceActions.__init__(self, proxy, None)
        tourne = TournerDroiteAction(proxy, angle, vitesse)
        avance_stop = AvanceJusquAuMur(proxy, vitesse)
        self.liste = [tourne, avance_stop]

def test_proximite_mur(proxy):
    return proxy.proximite_obstacle()