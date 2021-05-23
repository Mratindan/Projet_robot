import math
import time
from outils import Point, Vecteur
from modele import Polynome

class Robot_Exp:
    "Definition d'un robot"
    
    def __init__(self, a, b):
        """a et b ne doivent pas valoir 0 tous les deux"""
        assert(a != 0) or (b != 0)
        print("Creation d'un robot")
        self.x=a
        self.y=b
        self.xa=a
        self.ya=b
        self.xd=0
        self.yd=0
        self.positionNorme=0.
        self.positionNormeA=0.
        self.positionNormeD=0.
        self.vitesse=0.
        self.acceleration=0.
        self.positionVecteur=Vecteur(Polynome(0,0,a),Polynome(0,0,b))
        self.vitesseVecteur=Vecteur(Polynome(0,0,0),Polynome(0,0,0))
        self.accelerationVecteur=Vecteur(0,0)
        self.positionVecteurTemps=Vecteur(0,0)
        self.vitesseVecteurTemps=Vecteur(0,0)
        self.crayon=True
        self.last_update=0
        self.somme_temps=0
        self.distance=0
        self.diametre_robot=10
        
    def deplace(self, dx, dy):
        """
        int * int --> None
        Déplace le robot de dx en abscisse et dy en ordonnée.
        """
        self.x += dx
        self.y += dy
        print("Le robot s'est deplace en [", self.x, ",", self.y, "]")
        
    def affichePosition(self):
        """
        None --> None
        Affiche la position du robot.
        """
        print("Position du robot [", self.x, ",", self.y, "]")
            
    def changePosition(self,acceleration,angle):
        """
        float*float->None
        change le vecteur position du robot
        l'angle est lu dans le sens contraire des aiguilles d'une montre
        """
        self.somme_temps=time.time()-self.last_update
        self.x=self.positionVecteur.point1.calcul(self.somme_temps)
        self.y=self.positionVecteur.point2.calcul(self.somme_temps)
        self.positionVecteurTemps=Vecteur(self.x,self.y)
        self.positionNorme=math.sqrt(pow(self.positionVecteurTemps.point1,2)+pow(self.positionVecteurTemps.point2,2))
        self.xa=self.positionVecteur.point1.calcul(self.somme_temps-0.1)
        self.ya=self.positionVecteur.point2.calcul(self.somme_temps-0.1)
        if self.xa==self.x and self.ya==self.y:
            self.xa=0
            self.ya=0
        self.positionNormeA=math.sqrt(pow((self.positionVecteurTemps.point1-self.xa),2)+pow((self.positionVecteurTemps.point2-self.ya),2))
        self.vitesseVecteurTemps=Vecteur(self.vitesseVecteur.point1.calcul(self.somme_temps),self.vitesseVecteur.point2.calcul(self.somme_temps))
        self.vitesse=math.sqrt(pow(self.vitesseVecteurTemps.point1,2)+pow(self.vitesseVecteurTemps.point2,2))
        self.acceleration=acceleration
        self.accelerationVecteur.point1=(acceleration/self.positionNormeA)*((self.positionVecteurTemps.point1-self.xa)*math.cos(math.radians(angle))+(self.positionVecteurTemps.point2-self.ya)*math.sin(math.radians(angle)))
        self.accelerationVecteur.point2=(acceleration/self.positionNormeA)*(-(self.positionVecteurTemps.point1-self.xa)*math.sin(math.radians(angle))+(self.positionVecteurTemps.point2-self.ya)*math.cos(math.radians(angle)))
        self.vitesseVecteur=Vecteur(Polynome(0,self.accelerationVecteur.point1,self.vitesseVecteurTemps.point1),Polynome(0,self.accelerationVecteur.point2,self.vitesseVecteurTemps.point2))
        self.positionVecteur=Vecteur(Polynome(0.5*self.accelerationVecteur.point1,self.vitesseVecteurTemps.point1,self.positionVecteurTemps.point1),Polynome(0.5*self.accelerationVecteur.point2,self.vitesseVecteurTemps.point2,self.positionVecteurTemps.point2))
        
    def reset_time(self):
        """
        réinistialise le temps de départ
        """
        self.last_update=time.time()
        
    def distance_parcourue(self):
        """
        calcule la longueur de la trajectoire
        """
        self.somme_temps=time.time()-self.last_update
        self.xd=self.positionVecteur.point1.calcul(self.somme_temps)-self.positionVecteur.point1.calcul(self.somme_temps-0.1)
        self.yd=self.positionVecteur.point2.calcul(self.somme_temps)-self.positionVecteur.point2.calcul(self.somme_temps-0.1)
        self.distance+=abs(math.sqrt(pow(self.xd,2)+pow(self.yd,2)))
    
    def se_deplacer(self):
        """
        change les coordonnees x et y à chaque appel et met à jour la vitesse
        """
        self.somme_temps=time.time()-self.last_update
        self.x=self.positionVecteur.point1.calcul(self.somme_temps)
        self.y=self.positionVecteur.point2.calcul(self.somme_temps)
        self.xa=self.positionVecteur.point1.calcul(self.somme_temps+0.1)
        self.ya=self.positionVecteur.point2.calcul(self.somme_temps+0.1)
        self.vitesseVecteurTemps=Vecteur(self.vitesseVecteur.point1.calcul(self.somme_temps),self.vitesseVecteur.point2.calcul(self.somme_temps))
        self.vitesse=math.sqrt(pow(self.vitesseVecteurTemps.point1,2)+pow(self.vitesseVecteurTemps.point2,2))