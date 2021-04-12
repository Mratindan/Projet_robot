from modele import Robot_simple
from controleur import Controleur, Polygone, TriangleEq
from modele import Arene
from gui import Viewer
from math import pi

robot = Robot_simple(100,100)
deplaceRobotTriangle = TriangleEq(robot, 6)
controleur = Controleur(deplaceRobotTriangle)
deplaceRobotPolygone = Polygone(robot, 6)
controleur = Controleur(deplaceRobotPolygone)
arene = Arene(200,200, robot, controleur)
viewer = Viewer(arene)