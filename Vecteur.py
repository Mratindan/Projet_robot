import math
import numpy
from Point import Point
from numpy import *

class Vecteur:
    "Classe vecteur permettant de définir les déplacements de notre futur robot"

    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2

    def calculNorme(self):
        """
        None -> float
        Calcule la norme du vecteur
        """
        return math.sqrt(pow(self.point2.x-self.point1.x,2)+pow(self.point2.y-self.point1.y,2))

    def clonage(self):
        """
        None -> Vecteur
        Clone le vecteur
        """
        return Vecteur(Point(self.point1.x,self.point1.y),Point(self.point2.x,self.point2.y))

    def rotation(self):
        """
        None -> Vecteur
        Calcule la rotation d'un vecteur
        """
        R = numpy.array([(math.cos(x), -math.sin(x)),(math.sin(x),math.cos(x))])
        Vecteur2 = R * Vecteur()
        return Vecteur2

    def estEgal(self,Vecteur, Vecteur2):
        """
        Vecteur * Vecteur -> boolean
        Teste l'egalité entre deux vecteurs
        """
        if Vecteur==Vecteur2:
            return True
        return False

    def addition(self,v1)
        """
        Vecteur -> Vecteur
        Addition de deux vecteurs
        """
        return Vecteur(Point(self.point1.x+v1.point1.x,self.point1.y+v1.point1.y),Point(self.point2.x+v1.point2.x,self.point2.y+v1.point2.y))
    
    def scalaire(self,v1)
        """
        Vecteur -> float
        Produit scalaire entre deux vecteurs
        """
        return self.calculNorme()*v1.calculNorme()*math.cos(self.calculAngle(v1))
