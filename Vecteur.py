import math
#import numpy
from Point import Point
#from numpy import *

class Vecteur:
    "Classe vecteur permettant de définir les déplacements de notre futur robot"

    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2

    def __eq__(self, vecteur):
        return self.point1.x == vecteur.point1.x and self.point1.y == vecteur.point1.y and self.point2.x == vecteur.point2.x and self.point2.y == vecteur.point2.y

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

    def rotation(self,angle):
        """
        None -> Vecteur
        Calcule la rotation d'un vecteur
        """
        R = numpy.array([(math.cos(angle), -math.sin(angle)),(math.sin(angle),math.cos(angle))])
        Vecteur2 = R * Vecteur()
        return Vecteur2

    def estEgal(self, vecteur):
        """
        Vecteur * Vecteur -> boolean
        Teste l'egalité entre deux vecteurs
        """
        return vecteur == self

    def addition(self,v1):
        """
        Vecteur -> Vecteur
        Addition de deux vecteurs
        """
        return Vecteur(Point(self.point1.x+v1.point1.x,self.point1.y+v1.point1.y),Point(self.point2.x+v1.point2.x,self.point2.y+v1.point2.y))
    
    def produitVectoriel(self,v1):
        """
        Vecteur -> float
        Produit vectoriel du vecteur courant par v1.
        """
        return self.calculNorme()*v1.calculNorme()*math.cos(self.calculAngle(v1))

    def produitScalaire(self,v2,angle):
    	"""
		Permet de calculer le produit scalaire entre 2 vecteurs
    	"""
    	return self.calculNorme()*v2.calculNorme()*math.cos(angle)

# Test rapide constructeur de Point et Vecteur

p1 = Point(1, 2)
p2 = Point(3/4, -0.5)
p3 = Point(3,5)
p4 = Point(4,-3)

print("p1 : (", p1.x, ",", p1.y, ")")
print("p1 : (", p2.x, ",", p2.y, ")")

v1 = Vecteur(p1, p2)
v2 = Vecteur(p3,p4)
v3 = Vecteur(p1, p2)

#print("point1 de v : (", v.point1.x, ",", v.point1.y, ")")
#print("point2 de v : (", v.point2.x, ",", v.point2.y, ")")

print("PS entre v1 et v2 : ", v1.produitScalaire(v2,30))
print(