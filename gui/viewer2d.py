from tkinter import *
from tkinter import ttk

class Viewer :

    def __init__(self, arene):
        """
        Initialise une fenêtre graphique 
        """
        
        self.simulation = Tk()

        self.after_id = None
        self.arene = arene
        self.robot = self.arene.robot

        self.simulation.title("Gopigo Simulator")
        self.simulation.columnconfigure(0, weight = 1)
        self.simulation.rowconfigure(0, weight = 1)
        
        self.cadre = ttk.Frame(self.simulation)
        self.dessin_arene = Canvas(self.cadre, borderwidth = 2, relief = 'ridge', width = self.arene.width, height = self.arene.height, background = "white")

        self.cadre.grid(column = 0, row = 0, sticky = (N, S, E, W))
        self.dessin_arene.grid(column = 0, row = 0, columnspan = 6, rowspan = 6, sticky = (N, S, E, W))

        # Initialisation des dessins du robot et des obstacles 
        self.sommets_robot = (0, 0, 0, 0, 0, 0, 0, 0)
        self.trouver_sommets()
        self.dessin_robot_corps = self.dessin_arene.create_polygon(self.sommets_robot, fill = "orange", outline = "orange")
        self.dessiner_obstacles()
        self.dessin_robot_direction = self.dessin_arene.create_line(self.robot.x, self.robot.y, self.arene.robot_dirx, self.arene.robot_diry, fill = "brown", width = 2, arrow = "last")

    def trouver_sommets(self):
        """
        Permet de déterminer les coordonnées des sommets du carré qui représente le robot
        """
        x = self.robot.x
        y = self.robot.y
        m = self.robot.diametre_robot/2
        self.sommets_robot = (x - m, y - m, x - m, y + m, x + m, y + m, x + m, y - m)
    
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

        self.outil_crayon()
        self.trouver_sommets()
        self.dessin_arene.coords(self.dessin_robot_corps, self.sommets_robot)
        self.dessin_arene.coords(self.dessin_robot_direction, self.robot.x, self.robot.y, self.arene.robot_dirx, self.arene.robot_diry)
        self.after_id = self.dessin_arene.after(50, self.update)


    def lancer(self):
        """
        Lance l'interface graphique de la simulation
        """
        self.update()
        self.simulation.mainloop()
