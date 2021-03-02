from tkinter import *
from tkinter import ttk

class Sim :
    def __init__(self, x, y):
        """ Représente un objet avec une position initiale (x, y) """
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.dir = [1, 2]
    
    def controle_carre(self, l)
        """
        Fait "dessiner" un carré de côté l à l'objet.
        """
        




class Viewer :

    def __init__(self, simulation, objet):
        """
        simulation : Tk
        Initialise une fenêtre graphique 
        """

        # Variables nécessaires pour faire tourner la simulation
        self.after_id = None
        self.robot = objet

        # Nommage de la fenêtre principale de l'application
        simulation.title("Gopigo Simulator")
        # Détermination du comportement de la fenêtre lors des resize
        simulation.columnconfigure(0, weight = 1)
        simulation.rowconfigure(0, weight = 1)
        
        # Création des widgets :
        # Le cadre principale qui contiendra la toile, les boutons etc
        cadre = ttk.Frame(simulation)
        # La toile dans laquelle sera dessinée la simulation
        self.arene = Canvas(cadre, borderwidth = 2, relief = 'ridge', width = 600, height = 600, background = "white")
        # Les boutons
        play = ttk.Button(cadre, text = "Play", command = self.run)
        stop = ttk.Button(cadre, text = "Stop", command = self.stop)
        # Association de certaines touches du clavier à des commandes (en alternative aux boutons)
        simulation.bind("<Return>", lambda e: play.invoke())
        simulation.bind("<space>", lambda e: stop.invoke())


        # Placement des widgets
        cadre.grid(column = 0, row = 0, sticky = (N, S, E, W))
        self.arene.grid(column = 0, row = 0, columnspan = 6, rowspan = 6, sticky = (N, S, E, W))
        play.grid(column = 6, row = 3, sticky = (W, E))
        stop.grid(column = 8, row = 3, sticky = (W, E))

        # Initialisation des dessins du robot et des obstacles 
        self.dessin_robot = self.arene.create_rectangle(self.robot.x, self.robot.y, self.robot.x + self.robot.width, self.robot.y + self.robot.height, fill = 'red', outline = 'red')

        # Détermination du comportement du cadre lors des resize
        for i in range(6):
            cadre.columnconfigure(i, weight = 5)
            cadre.rowconfigure(i, weight = 1)
        for i in range(6, 9):
            cadre.columnconfigure(i, weight = 1)

    def update(self):
        """ 
        Permet de mettre à jour le dessin de la toile 
        """

        self.arene.coords(self.dessin_robot, self.robot.x, self.robot.y, self.robot.x + self.robot.width, self.robot.y + self.robot.height)

        # Permet de redessiner le terrain après un certain nombre de millisecondes
        self.after_id = self.arene.after(50, self.update)
    
    def run(self):
        """
        Permet de faire tourner la simulation
        """
        self.update()
    
    def stop(self):
       """
       Arrête la simulation
       """
       if self.after_id:
           self.arene.after_cancel(self.after_id)
           self.after_id = None

    def outil_crayon(self, objet):
        """
        Crayon pour un objet
        """



wall_e = Sim(200, 200)
simulation = Tk()
Viewer(simulation, wall_e)
simulation.mainloop()