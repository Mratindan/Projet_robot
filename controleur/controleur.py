import threading
import time
import math
from modele import Robot_simple


class Controleur(threading.Thread):
    def __init__(self, action):
        threading.Thread.__init__(self)
        self.action = action
        print("Le controleur a été initialisé !")

    def done(self):
        return self.action.done()

    def update(self):
        self.action.update()

    def demarre(self):
        self.action.demarre()

    def run(self): 
        print("Le controleur demande le démarrage.") 
        self.demarre() 
        print("Le controleur a été démarré avec succès !")
        while not (self.done()):
            print("Le controleur demande une mise à jour.")
            self.update()
            print("Le controleur a été mis à jour avec succès !")
            time.sleep(0.2)
            print("Le controleur demande si les actions sont terminés...", self.done())
            print("\n")
            

class SequenceActions:
    def __init__(self,robot,liste):
        self.liste = liste
        self.i = 0
        print("La séquence d'action a été initialisée !")

    def done(self):
        print("La séquence d'action vérifie qu'il reste des actions à effectuer...", "Est-ce que la liste d'action est arrivée à sa fin ?", self.i >= len(self.liste))
        return self.i >= len(self.liste)

    def update(self):
        print("Mise à jour de la séquence d'acion")
        if self.liste[self.i].done():
            print("Séquence action : l'action ", self.liste[self.i], "est fini !")
            self.i += 1
            if self.done(): 
                print("La séquence d'action est finie !")
                return None
            self.liste[self.i].demarre()
            print("Séquence action : l'action ", self.liste[self.i], "démarre !")
        self.liste[self.i].update()

    def demarre(self):
        self.i = 0
        self.liste[self.i].demarre()
        print(self.liste[self.i], "a démarré !")

class ParcourirAction:
    def __init__(self,robot,distance):
        self.robot = robot
        self.distance = distance
        self.vitesse = 1
        self.robot.reset_time()
        print("L'action Parcourir a été initialisée !")

    def done(self):
        print("L'action Parcourir vérifie la distance parcourue...")
        distance_parcourue = self.robot.distance_parcourue(self.robot.last_update)
        print("La distance parcourue est de ", distance_parcourue)
        return distance_parcourue > self.distance

    def update(self):
        if self.done(): 
            print("L'action Parcourir est fini !")
            return None
        self.robot.avance_tout_droit(1)
        print("L'action parcourir donne l'ordre au robot d'avancer tout droit !")

    def demarre(self):
        self.robot.reset_time()
        print("L'action Parcourir a démarrée !")


class TournerGaucheAction:
    def __init__(self,robot,angle):
        self.angle = angle
        self.vitesse = 50

    def done(self):
        angle = self.robot.angle_parcouru(self.robot.last_update)
        return angle > nouvel_angle

    def update(self):
        if self.done(): 
            return None
        self.robot.change_dir(0,self.vitesse)

    def demarre(self):
        self.robot.reset_time()

        
class Carre(SequenceActions):
    def __init__(self,robot):
        SequenceActions.__init__(self, robot, None)
        parcourir = ParcourirAction(robot, 1)
        #tourner = TournerGaucheAction(robot,90)
        #self.liste = [parcourir,tourner]*4
        self.liste = [parcourir]
        print("Le carré a été initialisé !")