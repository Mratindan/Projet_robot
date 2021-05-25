from modele import Robot_Exp, Arene
from controleur import Test, Test2, Test3, Test4, Tourner, Carre, Carre2, Controleur_Exp
from viewer import Viewer

def start_simulation(arene, interface_graphique) :
    arene.controleur.start()
    arene.start()
    interface_graphique.lancer()

# Notre robot
wall_e=Robot_Exp(200, 400)

# Notre action à donner au controleur
dessine=Carre2(wall_e)
#dessine = Test(wall_e)
#dessine = Test2(wall_e)
#dessine = Test3(wall_e)
#dessine = Test4(wall_e)

# Controleur
ctrl=Controleur_Exp(dessine)

# Arene
arene=Arene(800, 800, wall_e, ctrl, 0, 0)

# Viewer
interface_graphique=Viewer(arene)

# On lance la simulation
start_simulation(arene, interface_graphique)