from modele import Robot_simple
import controleur
from modele import Arene
from gui import Viewer 


def start_simulation(arene, interface_graphique) :
    arene.controleur.start()
    arene.start()
    interface_graphique.lancer()

# Notre robot
wall_e = Robot_simple(200, 200)

# Notre action à donner au contrôleur
dessine = controleur.Polygone(wall_e,5)

# Controleur
ctrl = controleur.Controleur(dessine)

# Arene
arene = Arene(600, 600, wall_e, ctrl)

# Viewer
interface_graphique = Viewer(arene)

# On lance la simulation
start_simulation(arene, interface_graphique)