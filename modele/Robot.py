import math
from Point import Point
from Vecteur import Vecteur
from Polynome import Polynome

class Robot :
    "Definition d'un robot"
    
    def __init__(self, a, b):
        print("Creation d'un robot")
        self.position = Point(a, b)
        self.positionNorme=0.
        self.vitesse = 0.
        self.acceleration=0.
        self.positionVecteur=Vecteur(Polynome(0,0,1),Polynome(0,0,1))
        self.vitesseVecteur=Vecteur(Polynome(0,0,0),Polynome(0,0,0))
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
        change le vecteur mouvement du robot
        l'angle est lu dans le sens des aiguilles d'une montre
        """
        self.position.x=self.positionVecteur.point1.calcul(temps)
        self.position.y=self.positionVecteur.point2.calcul(temps)
        self.positionVecteurTemps=Vecteur(self.position.x,self.position.y)
        self.positionNorme=math.sqrt(pow(self.positionVecteurTemps.point1,2)+pow(self.positionVecteurTemps.point2,2))
        self.vitesseVecteurTemps=Vecteur(self.vitesseVecteur.point1.calcul(temps),self.vitesseVecteur.point2.calcul(temps))
        self.vitesse=math.sqrt(pow(self.vitesseVecteurTemps.point1,2)+pow(self.vitesseVecteurTemps.point2,2))
        self.acceleration=acceleration
        self.accelerationVecteur.point1=(acceleration/self.positionNorme)*((self.positionVecteurTemps.point1)*math.cos(angle)+(self.positionVecteurTemps.point2)*math.sin(angle))
        self.accelerationVecteur.point2=(acceleration/self.positionNorme)*(-(self.positionVecteurTemps.point1)*math.sin(angle)+(self.positionVecteurTemps.point2)*math.cos(angle))
        #utiliser methode rotation de la classe vecteur? (tester d'abord) -> pas de changment de norme
        self.vitesseVecteur=Vecteur(Polynome(0,self.accelerationVecteur.point1,self.vitesseVecteurTemps.point1),Polynome(0,self.accelerationVecteur.point2,self.vitesseVecteurTemps.point2))
        self.positionVecteur=Vecteur(Polynome(0.5*self.accelerationVecteur.point1,self.vitesseVecteurTemps.point1,self.positionVecteurTemps.point1),Polynome(0.5*self.accelerationVecteur.point2,self.vitesseVecteurTemps.point2,self.positionVecteurTemps.point2))
        #creer une methode pour transformer le vecteur position en fonction utilisable
        