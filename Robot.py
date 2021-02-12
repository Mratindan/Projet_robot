import math
from Point import Point
from Vecteur import Vecteur

class Robot :
    "Definition d'un robot"
    
    def __init__(self, a, b):
        print("Creation d'un robot")
        self.position = Point(a, b)
        self.vitesse = 0.
        self.acceleration=0.
        self.positionVecteur=Vecteur(0,0)
        self.vitesseVecteur=Vecteur(0,0)
        self.accelerationVecteur=Vecteur(0,0)
        self.positionVecteurTemps=Vecteur(0,0)
        self.vitesseVecteurTemps=Vecteur(0,0)
        
    def deplace(self, dx, dy):
        """
        int * int --> None
        Déplace le robot de dx en abscisse et dy en ordonnée.
        """
        self.position.x += dx
        self.position.y += dy
        print("Le robot s'est deplace en [", self.position.x, ",", self.position.y, "]")
        
    def affichePosition(self):
        """
        None --> None
        Affiche la position du robot.
        """
        print("Position du robot [", self.position.x, ",", self.position.y, "]")
            
    def changePosition(self,acceleration,angle,temps):
        """
        float*float->None
        change la fonction caractérisant le mouvement du robot
        """
        self.position.x=self.positionVecteur.x.calcul(temps)
        self.position.y=self.positionVecteur.y.calcul(temps)
        self.positionVecteurTemps=Vecteur(self.position.x,self.position.y)
        #faire classe polynome avec methode calcul en fonction du temps
        
        
        
