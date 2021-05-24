from controleur.controleur import AvanceJusquAuMurPuisNouvelleDirection, ParcourirAction
from modele import Robot
try:
    from Robot2I013 import Robot2I013
    raise Exception("Le robot 2I013 n'existe pas.")
except Exception as e:
    from robotmockup import Robot2I013Mockup
from controleur import Proxy_simu, Proxy_irl, Controleur
from controleur import Carre, AvanceJusquAuMur, TourneAvanceStop, AvanceJusquAuMurPuisNouvelleDirection, BoucleSurTourne, ParcoursAutonome, ParcourirAction
from modele import Arene
from viewer import Viewer 

def start_simulation(arene, interface_graphique) :
    arene.controleur.start()
    arene.start()
    interface_graphique.lancer()

# Notre robot
wall_e = Robot(200, 300)

# Notre proxy
wall_e_simu = Proxy_simu(wall_e)

# Notre action à donner au contrôleur
action = ParcoursAutonome(wall_e_simu, 5, 12)

# Controleur
ctrl = Controleur(wall_e_simu, action)

# Arene
arene = Arene(800, 800, wall_e, ctrl, 100, 50)

# On donne l'arene au proxy
wall_e_simu.arene = arene

# Viewer
interface_graphique = Viewer(arene)

# On lance la simulation
start_simulation(arene, interface_graphique)