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
        
        # Le cadre principale de l'application
        self.cadre = ttk.Frame(self.simulation)
        # La toile dans laquelle sera dessinée la simulation
        self.dessin_arene = Canvas(self.cadre, borderwidth = 2, relief = 'ridge', width = self.arene.width, height = self.arene.height, background = "white")

        # Placement des widgets
        self.cadre.grid(column = 0, row = 0, sticky = (N, S, E, W))
        self.dessin_arene.grid(column = 0, row = 0, columnspan = 6, rowspan = 6, sticky = (N, S, E, W))

        # Initialisation des dessins du robot et des obstacles 
        self.dessin_robot_corps = self.dessin_arene.create_rectangle(self.robot.x, self.robot.y, self.robot.x + self.robot.diametre_robot, self.robot.y + self.robot.diametre_robot, fill = 'red', outline = 'red')
        self.dessiner_obstacles()
    
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
        self.dessin_arene.coords(self.dessin_robot_corps, self.robot.x, self.robot.y, self.robot.x + self.robot.diametre_robot, self.robot.y + self.robot.diametre_robot)
        self.after_id = self.dessin_arene.after(50, self.update)


    def lancer(self):
        """
        Lance l'interface graphique de la simulation
        """
        self.update()
        self.simulation.mainloop()
    
    def stop(self):
       """
       Arrête la simulation (Non fonctionnel pour l'instant)
       """
       if self.after_id:
           self.dessin_arene.after_cancel(self.after_id)
           self.after_id = None