import math

class Point:
	"Classe permettant de définir des points"

	def __init__(self,x,y):
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


point1 = Point(1,2)
point2 = Point(4,6)

point3 = Point(-2,-1)
point4 = Point(6,-3)


print("Distance entre les points (1,2) et (4,6) = ", point1.distance(point2))
print("Distance entre les points (-2,-1) et (6,-3) = ", point4.distance(point3))
