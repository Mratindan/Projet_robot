from gui.viewer import *
from modele.obstacle import *

# La simulation (c'est ce script qui est à déplacer dans simulation.py quand ce sera possible) 

# Notre robot
wall_e = Robot_tmp(200, 200)

# Controleur
ctrl = Controleur_carre(wall_e)

# Arene
arene = Arene_tmp(600, 600, wall_e, ctrl)

# Viewer
interface_graphique = Viewer(arene)

# On lance l'interface graphique et à partir de là on pourra appuyer sur play pour lancer les threads controleur et arene
interface_graphique.lancer()