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

	def rotation(self,angle,norme):
		"""
		None -> Vecteur
		Calcule la rotation d'un vecteur
		"""
		R = numpy.array([(math.cos(angle), -math.sin(angle)),(math.sin(angle),math.cos(angle))])
		Vecteur2 = R * Vecteur()
		Vecteur2.point1=Vecteur2.point1*(norme/self.calculNorme())
		Vecteur2.point2=Vecteur2.point2*(norme/self.calculNorme())
		return Vecteur2

	def estEgal(self,Vecteur2):
		"""
		Vecteur * Vecteur -> boolean
		Teste l'egalité entre deux vecteurs
		"""
		return self == Vecteur2

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

	def produitScalaire(self,v2):
		"""
		Permet de retourner le produit scalaire entre 2 vecteurs
		"""

		if type(self.point1) != type(v2.point1):
			print("Erreur, l'objet sur lequel est appelée la méthode, et l'argument ne sont pas définis de la même façon.")
			return
		else:
			if isinstance(self.point1,int) and isinstance(v2.point1,int):
				return self.point1 * v2.point1 + self.point2 * v2.point2
			else:
				return (self.point2.getX()-self.point1.getX())*(v2.point2.getX()-v2.point1.getX()) + (self.point2.getY()-self.point1.getY())*(v2.point2.getY()-v2.point1.getY())

	def calculAngle(self,v2):
		"""
		Permet de récupérer l'angle (en °) entre 2 vecteurs, à partir de son produit scalaire
		"""
		if type(self.point1) != type(v2.point1):
			print("Erreur, l'objet sur lequel est appelée la méthode, et l'argument ne sont pas définis de la même façon.")
			return
		else:
			if isinstance(self.point1,int) and isinstance(v2.point1,int):
				return (math.acos((self.point1*v2.point1 + self.point2*v2.point2)/(math.sqrt(((self.point1)**2)+((self.point2)**2))*math.sqrt(((v2.point1)**2)+((v2.point2)**2)))))*(180/math.pi)
			else:
				return (math.acos(((self.produitScalaire(v2) / (self.calculNorme() * v2.calculNorme())))))*(180/math.pi)