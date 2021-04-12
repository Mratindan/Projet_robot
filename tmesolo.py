from modele import Robot_simple
from controleur import Controleur, Exo1, Exo2_TriangleEqui
from modele import Arene
from gui import Viewer

def start_simulation(arene, interface_graphique) :
    arene.controleur.start()
    arene.start()
    interface_graphique.lancer()

wall_e = Robot_simple(200, 200)

# Exercice 1
#exo1 = Exo1(wall_e)
#ctrl_exo1 = Controleur(exo1)
#arene = Arene(600, 600, wall_e, ctrl_exo1)

# Exercice 2.1
exo2q1 = Exo2_TriangleEqui(wall_e)
ctrl_exo2q1 = Controleur(exo2q1)
arene = Arene(600, 600, wall_e, ctrl_exo2q1)






interface_graphique = Viewer(arene)
start_simulation(arene, interface_graphique)

