import viewer
import modele
import arene

# La simulation (c'est ce script qui est à déplacer dans simulation.py quand ce sera possible) 

# Notre robot
wall_e = Robot_simple(200, 200)

# Controleur
ctrl = Controleur_carre(wall_e)

# Arene
arene = Arene_tmp(600, 600, wall_e, ctrl)

# Viewer
interface_graphique = Viewer(arene)

# On lance l'interface graphique et à partir de là on pourra appuyer sur play pour lancer les threads controleur et arene
interface_graphique.lancer()