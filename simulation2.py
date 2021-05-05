from modele import Robot, Robot_simple, Arene
from controleur import *
from gui import Viewer

def start_simulation(arene, interface_graphique) :
    arene.controleur.start()
    arene.start()
    interface_graphique.lancer()

# Notre robot
wall_e=Robot(200, 200)

# Notre action à donner au contrôleur
dessine=Test(wall_e)

# Controleur
ctrl=Controleur(dessine)

# Arene
arene=Arene(600, 600, wall_e, ctrl)

# Viewer
interface_graphique=Viewer(arene)

# On lance la simulation
start_simulation(arene, interface_graphique)