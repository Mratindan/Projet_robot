from modele import Robot_simple
from controleur import Proxy_simu, Proxy_irl, Carre, Controleur
from modele import Arene
from gui import Viewer 

def start_simulation(arene, interface_graphique) :
    arene.controleur.start()
    arene.start()
    interface_graphique.lancer()

# Notre robot
wall_e = Robot_simple(200, 200)

# Notre proxy
wall_e_simu = Proxy_simu(wall_e)

# Notre action à donner au contrôleur
dessine = Carre(wall_e_simu)

# Controleur
ctrl = Controleur(dessine)

# Arene
arene = Arene(600, 600, wall_e, ctrl)

# Viewer
interface_graphique = Viewer(arene)

# On lance la simulation
start_simulation(arene, interface_graphique)