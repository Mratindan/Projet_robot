from modele import *
from controleur import *
from gui import Viewer

def start_simulation(arene, interface_graphique) :
    arene.controleur.start()
    arene.start()
    interface_graphique.lancer()

# Notre robot
wall_e = Robot_simple(200, 200)
wall_e2=Robot(200, 200)
# Notre action à donner au contrôleur
dessine = Carre(wall_e)
dessine2=Test(wall_e2)

# Controleur
ctrl = Controleur(dessine)
ctrl2=Controleur(dessine2)

# Arene
arene = Arene(600, 600, wall_e, ctrl)
arene2=Arene(600, 600, wall_e2, ctrl2)

# Viewer
interface_graphique = Viewer(arene)
interface_graphique2=Viewer(arene2)

# On lance la simulation
#start_simulation(arene, interface_graphique)
start_simulation(arene2, interface_graphique2)