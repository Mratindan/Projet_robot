from modele import Robot_simple
from controleur import Controleur, Exo1, Exo2_TriangleEqui, Exo2_Polygone
from modele import Arene
from gui import Viewer

def start_simulation(arene, interface_graphique) :
    arene.controleur.start()
    arene.start()
    interface_graphique.lancer()

wall_e = Robot_simple(200, 200)

# Exercice 1
#exo1 = Exo1(wall_e) # Action qu'on veut donner au controleur
#ctrl_exo1 = Controleur(exo1)
#arene = Arene(600, 600, wall_e, ctrl_exo1)

# Exercice 2.1
#exo2q1 = Exo2_TriangleEqui(wall_e)
#ctrl_exo2q1 = Controleur(exo2q1)
#arene = Arene(600, 600, wall_e, ctrl_exo2q1)

# Exercice 2.2
robot = Robot_simple(200, 300)
exo2q2 = Exo2_Polygone(robot, 8)
ctrl_exo2q2 = Controleur(exo2q2)
arene = Arene(600, 600, robot, ctrl_exo2q2)






interface_graphique = Viewer(arene)
start_simulation(arene, interface_graphique)

