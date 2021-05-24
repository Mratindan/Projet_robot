from modele import Robot_Exp, Robot_simple, Arene
from controleur import Test, Test2, Test3, Test4, Tourner, Carre, Carre2, Controleur_Exp
from gui import Viewer

def start_simulation(arene, interface_graphique) :
    arene.controleur.start()
    arene.start()
    interface_graphique.lancer()

# Notre robot
wall_e=Robot_Exp(300, 300)

# Notre action à donner au controleur
dessine=Carre2(wall_e)
#dessine = Test(wall_e)
#dessine = Test2(wall_e)
#dessine = Test3(wall_e)
#dessine = Test4(wall_e)

# Controleur
ctrl=Controleur_Exp(dessine)

# Arene
arene=Arene(600, 600, wall_e, ctrl, 10, 50)

# Viewer
interface_graphique=Viewer(arene)

# On lance la simulation
start_simulation(arene, interface_graphique)