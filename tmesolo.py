from modele import Robot_simple
from controleur import Carre, Controleur
from modele import Arene
from gui import Viewer 
from math import pi


def start_simulation(arene, interface_graphique) :
    arene.controleur.start()
    arene.start()
    interface_graphique.lancer()

#On crée notre robot
wall_e = Robot_simple(200, 200)

dessine = Carree(wall_e,5)

# Controleur
ctrl = Controleur(dessine)

# Arene
arene = Arene(600, 600, wall_e, ctrl)

# Viewer
interface_graphique = Viewer(arene)

# On lance la simulation
start_simulation(arene, interface_graphique)