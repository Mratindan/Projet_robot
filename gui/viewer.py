from tkinter import *
from tkinter import ttk

class Viewer :

    def __init__(self, simulation):
        """
        simulation : Tk
        Initialise une fenêtre graphique 
        """

        # Variables nécessaires pour faire tourner la simulation
        self.after_id = None

        # Création de la fenêtre principale de l'application
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


        # Détermination du comportement du cadre lors des resize
        for i in range(6):
            cadre.columnconfigure(i, weight = 5)
            cadre.rowconfigure(i, weight = 1)
        for i in range(6, 9):
            cadre.columnconfigure(i, weight = 1)


        # Essai provisoire : création d'un rectangle qui se déplace continuellement
        self.width = 20
        self.height = 20
        self.x = 0
        self.y = 0
        self.dx = 2
        self.dy = 1
        self.robot = self.arene.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill = 'red', outline = 'red')

    def update(self):
        """ 
        Permet de mettre à jour le dessin de la toile 
        """
        self.x += self.dx 
        self.y += self.dy

        self.arene.coords(self.robot, self.x, self.y, self.x + self.width, self.y + self.height)

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
        

simulation = Tk()
Viewer(simulation)
simulation.mainloop()