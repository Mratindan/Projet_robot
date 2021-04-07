class Obstacle:
	"""Definition de la classe obstacle"""
	def __init__(self,largeur,hauteur):
		assert (largeur != 0) or (hauteur != 0), "Un obstacle ne peut pas avoir des tailles nulles"
		self.largeur = largeur
		self.hauteur = hauteur
