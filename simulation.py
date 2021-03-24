from gui import Viewer 
from modele import Arene, Robot_simple
from controleur import Controleur_carre

def start_simulation(arene, interface_graphique) :
            arene.controleur.start()
            arene.start()
            interface_graphique.lancer()

# Notre robot
wall_e = Robot_simple(200, 200)

# Controleur
ctrl = Controleur_carre(wall_e)

# Arene
arene = Arene(600, 600, wall_e, ctrl)

# Viewer
interface_graphique = Viewer(arene)

# On lance la simulation
start_simulation(arene, interface_graphique)