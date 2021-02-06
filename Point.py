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



