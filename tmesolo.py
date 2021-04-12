from modele import Robot_simple
from controleur import Carre, Controleur,Triangle,Polygone
from modele import Arene
from gui import Viewer 
from math import pi


def q2_1():
	def start_simulation(arene, interface_graphique) :
	    arene.controleur.start()
	    arene.start()
	    interface_graphique.lancer()

	#On crée notre robot
	wall_e = Robot_simple(200, 200)

	dessine = Triangle(wall_e)

	# Controleur
	ctrl = Controleur(dessine)

	# Arene
	arene = Arene(600, 600, wall_e, ctrl)

	# Viewer
	interface_graphique = Viewer(arene)

	# On lance la simulation
	start_simulation(arene, interface_graphique)

def q2_2():
	def start_simulation(arene, interface_graphique) :
	    arene.controleur.start()
	    arene.start()
	    interface_graphique.lancer()

	#On crée notre robot
	wall_e = Robot_simple(200, 200)

	dessine = Polygone(wall_e,8)

	# Controleur
	ctrl = Controleur(dessine)

	# Arene
	arene = Arene(600, 600, wall_e, ctrl)

	# Viewer
	interface_graphique = Viewer(arene)

	# On lance la simulation
	start_simulation(arene, interface_graphique)


#q2_1 : Triangle
q2_1()

#q2_2 : Polygone (Octogone)
#q2_2()