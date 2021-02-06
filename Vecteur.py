import math
from Point import Point

class Vecteur:
    "Classe vecteur permettant de définir les déplacements de notre futur robot"
    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2
    def calculNorme(self):
        "Calcule la norme du vecteur"
        return math.sqrt(pow(self.point2.x-self.point1.x,2)+pow(self.point2.y-self.point1.y,2))
    def clonage(self):
        "Clone le vecteur"
        return Vecteur(Point(self.point1.x,self.point1.y),Point(self.point2.x,self.point2.y))
