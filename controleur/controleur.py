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


class ConditionActions:
    def __init__(self, action_principale, action_alternative, condition):
        self.action_principale = action_principale
        self.action_alternative = action_alternative
        print("ConditionActions a été initialisé")

    def done(self):
        print("ConditionActions...l'action principale est terminée : ", self.action_principale.done())
        print("ConditionActions...l'action alternative est terminée : ", self.action_alternative.done())
        return self.action_principale.done() or self.action_alternative.done()

    def update(self):
        print("ConditionActions essaie de se mettre à jour...")
        if self.done(): 
            print("ConditionActions est terminé")
            return None
        print("Condition[0] : ", self.condition[0]())
        if self.condition[0]():
            print("La condition de ConditionActions est vérifiée")
            if not self.action_alternative.est_en_cours:
                print("ConditionActions démarre la condition alternative")
                self.action_alternative.demarre()
                self.action_alternative.est_en_cours = True
            print("ConditionActions demande la mise à jour de l'action alternative")
            self.action_alternative.update()
        else : 
            print("ConditionActions demande la mise à jour de l'action principale")
            self.action_principale.update()

    def demarre(self):
        self.action_principale.demarre()
        print("L'action principale de ConditionActions a démarré")


class ParcourirAction:
    def __init__(self, proxy, distance, vitesse):
        self.proxy = proxy
        self.distance = distance
        self.vitesse = vitesse

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
    def __init__(self, proxy, angle, vitesse):
        self.proxy = proxy
        self.angle = angle
        self.vitesse = vitesse

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
    def __init__(self, proxy, angle, vitesse):
        self.proxy = proxy
        self.angle = angle
        self.vitesse = vitesse

    def done(self):
        angle_parcouru = self.proxy.angle_parcouru_gauche(self.proxy.last_update)
        return angle_parcouru > self.angle

    def update(self):
        if self.done(): 
            return None
        self.proxy.tourne_gauche(self.vitesse)

    def demarre(self):
        self.proxy.reset_time()

class StopAction:
    def __init__(self, proxy):
        self.proxy = proxy
        self.est_en_cours = False
        self.t = None

    def done(self):
        if not self.est_en_cours :
            return False
        distance_parcourue = self.proxy.distance_parcourue(self.t)
        print("StopAction : la distance parcourue depuis le démarrage de StopAction est : ", distance_parcourue)
        return distance_parcourue == 0
    
    def update(self):
        if self.done():
            return None
        if (time.time() - self.t) > 2 :
            self.t = time.time()
    
    def demarre(self):
        self.t = time.time()
        self.proxy.stop()

class AvanceJusquAuMur(ConditionActions):
    def __init__(self, proxy):
        ConditionActions.__init__(self, None, None, None)
        self.action_principale = ParcourirAction(proxy, 1000, 5)
        self.action_alternative = StopAction(proxy)
        self.condition = [lambda : proxy.proximite_mur()]

class Carre(SequenceActions):
    def __init__(self, proxy, longueur_cote, vitesse_deplacement, vitesse_rotation):
        SequenceActions.__init__(self, None)
        parcourir = ParcourirAction(proxy, longueur_cote, vitesse_deplacement)
        tourner_droite = TournerDroiteAction(proxy, 90, vitesse_rotation)
        self.liste = [parcourir, tourner_droite] * 3 + [parcourir]

class TourneAvanceStop(SequenceActions):
    def __init__(self, proxy):
        SequenceActions.__init__(self, None)
        tourne = TournerDroiteAction(proxy, 180, 15)
        avance_stop = AvanceJusquAuMur(proxy)
        self.liste = [tourne, avance_stop]