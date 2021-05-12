from tkinter import *
from tkinter import ttk
import math
from modele import Robot_simple, Arene

class Viewer :

    def __init__(self, arene):
        """
        Initialise une fenêtre graphique 
        """
        
        self.simulation = Tk()

        self.arene = arene
        self.robot = self.arene.robot
        self.angle_prec = self.robot.angle

        self.simulation.title("Gopigo Simulator")
        # Détermination du comportement de la fenêtre lors des resize
        self.simulation.columnconfigure(0, weight = 1)
        self.simulation.rowconfigure(0, weight = 1)
        
        # Création des widgets :
        # Le cadre principale qui contiendra la toile, les boutons etc
        self.cadre = ttk.Frame(self.simulation)
        # La toile dans laquelle sera dessinée la simulation
        self.dessin_arene = Canvas(self.cadre, borderwidth = 2, relief = "ridge", width = self.arene.width, height = self.arene.height, background = "white")

        # Placement des widgets
        self.cadre.grid(column = 0, row = 0, sticky = (N, S, E, W))
        self.dessin_arene.grid(column = 0, row = 0, sticky = (N, S, E, W))

        # Initialisation des dessins du robot et des obstacles 
        self.sommets_robot = (0, 0, 0, 0, 0, 0, 0, 0)
        self.trouver_sommets()
        self.dessin_robot_corps = self.dessin_arene.create_polygon(self.sommets_robot, fill = "orange", outline = "orange")
        self.direction_robot = (self.robot.x, self.robot.y, self.robot.x, self.robot.y - 2 * self.robot.diametre_robot)
        self.dessin_robot_tete = self.dessin_arene.create_line(self.direction_robot, fill = "orange", width = "5", arrow = "last")
        self.dessiner_obstacles()

    def trouver_direction(self, a):
        """
        Permet de déterminer les coordonnées du segment qui représente la direction du robot
        """
        x0, y0, x1, y1 = self.direction_robot
        nx1, ny1 = self.rotation_point(x1, y1, x0, y0, a - self.angle_prec)
        self.direction_robot = (self.robot.x, self.robot.y, nx1, ny1)

    def trouver_sommets(self):
        """
        Permet de déterminer les coordonnées des sommets du carré qui représente le robot
        """
        x = self.robot.x
        y = self.robot.y
        m = self.robot.diametre_robot/2
        self.sommets_robot = (x - m, y - m, x - m, y + m, x + m, y + m, x + m, y - m)

    def pivoter_robot(self, a):
        """
        Permet de déterminer le dessin du robot après une rotation.
        Concrétement on met à jour la liste des coordonnées des sommets du carré.
        """
        cx = self.robot.x
        cy = self.robot.y
        angle = math.radians(a - self.angle_prec)

        x1, y1, x2, y2, x3, y3, x4, y4 = self.sommets_robot
        nx1, ny1 = self.rotation_point(x1, y1, cx, cy, angle)
        nx2, ny2 = self.rotation_point(x2, y2, cx, cy, angle)
        nx3, ny3 = self.rotation_point(x3, y3, cx, cy, angle)
        nx4, ny4 = self.rotation_point(x4, y4, cx, cy, angle)
        self.sommets_robot = (nx1, ny1, nx2, ny2, nx3, ny3, nx4, ny4)

    def rotation_point(self, x, y, cx, cy, angle):
        """
        Permet de faire pivoter x et y autour du centre du carré selon l'angle 
        """
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)

        tmpx = x - cx
        tmpy = y - cy

        rx = tmpx * cos_angle - tmpy * sin_angle
        ry = tmpx * sin_angle + tmpy * cos_angle

        nx = rx + cx
        ny = ry + cy

        return (nx, ny)


    def dessiner_obstacles(self):
        """
        Dessine les obstacles à partir de la liste self.arene.list_obstacles
        """
        for obstacle in self.arene.liste_obstacles :
            self.dessin_arene.create_rectangle(obstacle.x, obstacle.y, obstacle.x + obstacle.width, obstacle.y + obstacle.height, fill = 'black', outline = 'black')
    
    def outil_crayon(self):
        """
        Crayon pour un robot, dessine à l'endroit où il se trouve
        """
        if self.robot.crayon :
            self.dessin_arene.create_line(self.robot.x, self.robot.y, self.robot.x + 1, self.robot.y + 1, fill='green', width=3)
        
    def update(self):
        """ 
        Permet de mettre à jour le dessin de la toile 
        """
        print(self.robot.angle)
        self.outil_crayon()
        if self.angle_prec == self.robot.angle:
            self.trouver_sommets()
        else:
            self.pivoter_robot(self.robot.angle)
        self.dessin_arene.coords(self.dessin_robot_corps, self.sommets_robot)

        self.trouver_direction(self.robot.angle)
        self.dessin_arene.coords(self.dessin_robot_tete, self.direction_robot)

        self.angle_prec = self.robot.angle
        self.dessin_arene.after(50, self.update)


    def lancer(self):
        """
        Lance l'interface graphique de la simulation
        """
        self.update()
        self.simulation.mainloop()