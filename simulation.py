import gui
import modele
import controleur

# La simulation (c'est ce script qui est à déplacer dans simulation.py quand ce sera possible) 

# Notre robot
wall_e = modele.robot_simple.Robot_simple(200, 200)

# Controleur
ctrl = controleur.controleur_robot.Controleur_carre(wall_e)

# Arene
arene = modele.arene.Arene(600, 600, wall_e, ctrl)

# Viewer
interface_graphique = gui.viewer.Viewer(arene)

# On lance l'interface graphique et à partir de là on pourra appuyer sur play pour lancer les threads controleur et arene
interface_graphique.lancer()