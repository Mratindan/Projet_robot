from modele import Robot_simple
from controleur import Carre, Controleur, Exo1
from modele import Arene
from gui import Viewer

def start_simulation(arene, interface_graphique) :
    arene.controleur.start()
    arene.start()
    interface_graphique.lancer()

wall_e = Robot_simple(200, 200)

# Exercice 1
exo1 = Exo1(wall_e)
ctrl_exo1 = Controleur(exo1)
arene = Arene(600, 600, wall_e, ctrl_exo1)
interface_graphique = Viewer(arene)
start_simulation(arene, interface_graphique)

