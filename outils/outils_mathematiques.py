# -*- coding: utf-8 -*-
import math

class Point:
	"Classe permettant de définir des points "

	def __init__(self,x,y):
		"""Initialise un point aux coordonées (x,y)"""
		self.x = x
		self.y = y

	def distance(self, point):
		"""
		Point -> float
		Retourne la distance entre le point courant et le point en parametre.
		"""
		return math.sqrt((point.x - self.x) * (point.x - self.x) + (point.y - self.y) * (point.y - self.y))
	
	def getX(self):
		return self.x

	def getY(self):
		return self.y

class Vecteur:
	"Classe vecteur permettant de définir les déplacements de notre futur robot"

	def __init__(self,point1,point2):
		"""Définition d'un vecteur à partir de 2 points"""
		self.point1 = point1
		self.point2 = point2

	def __init__(self,x,y):
		"""Définition d'un vecteur à partir de coordonées"""
		self.point1 = x
		self.point2 = y

	def __eq__(self, Vecteur2):
		return self.point1.x == Vecteur2.point1.x and self.point1.y == Vecteur2.point1.y and self.point2.x == Vecteur2.point2.x and self.point2.y == Vecteur2.point2.y

	def addition(self,v1):
		"""
		Vecteur -> Vecteur
		Addition de deux vecteurs
		"""
		return Vecteur(Point(self.point1.x+v1.point1.x,self.point1.y+v1.point1.y),Point(self.point2.x+v1.point2.x,self.point2.y+v1.point2.y))

class Polynome:
    "Construit un polynome de degré 2 de forme: a*(x^2)+b*x+c"
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def calcul(self,x):
        return (self.a*pow(x,2)+self.b*x+self.c)
    def affichePolynome(self,x):
        print(self.a,x,"^2 +",self.b,x,"+",self.c)