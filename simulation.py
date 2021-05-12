from modele import Robot_simple
try:
    from Robot2I013 import Robot2I013
    raise Exception("Le robot 2I013 n'existe pas.")
except Exception as e:
    from robotmockup import Robot2I013Mockup
from controleur import Proxy_simu, Proxy_irl, Carre, AvanceJusquAuMur, TourneAvanceStop, Controleur
from modele import Arene
from gui import Viewer 

def start_simulation(arene, interface_graphique) :
    arene.controleur.start()
    arene.start()
    interface_graphique.lancer()

# Notre robot
wall_e = Robot_simple(200, 300)

# Notre proxy
wall_e_simu = Proxy_simu(wall_e)

# Notre action à donner au contrôleur
action = Carre(wall_e_simu, 0.5, 5, 10)

# Controleur
ctrl = Controleur(wall_e_simu, action)

# Arene
arene = Arene(1200, 600, wall_e, ctrl, 10, 50)

# Viewer
interface_graphique = Viewer(arene)

# On lance la simulation
start_simulation(arene, interface_graphique)