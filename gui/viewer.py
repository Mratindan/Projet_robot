from tkinter import *
from tkinter import ttk

class Arene_tmp :
    """
    En attendant qu'il y ait les import nécessaires pour utiliser un objet arene ici. 
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

class Sim :
    def __init__(self, x, y):
        """ Représente un objet avec une position initiale (x, y) """
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.dir = [1, 0]
    
    def change_dir(self, dx, dy):
        self.dir[0] = dx
        self.dir[1] = dy
    

class Viewer :

    def __init__(self, simulation, objet, arene):
        """
        simulation : Tk
        Initialise une fenêtre graphique 
        """

        # Variables nécessaires pour faire tourner la simulation
        self.after_id = None
        self.robot = objet
        self.cpt = 0
        self.modele_arene = arene

        # Nommage de la fenêtre principale de l'application
        simulation.title("Gopigo Simulator")
        # Détermination du comportement de la fenêtre lors des resize
        simulation.columnconfigure(0, weight = 1)
        simulation.rowconfigure(0, weight = 1)
        
        # Création des widgets :
        # Le cadre principale qui contiendra la toile, les boutons etc
        cadre = ttk.Frame(simulation)
        # La toile dans laquelle sera dessinée la simulation
        self.arene = Canvas(cadre, borderwidth = 2, relief = 'ridge', width = self.modele_arene.width, height = self.modele_arene.height, background = "white")
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
    
    def dessiner_obstacles():
        """
        Dessine les obstacles à partir de la liste self.arene_modele.list_obstacles
        """

    def update(self):
        """ 
        Permet de mettre à jour le dessin de la toile 
        """

        self.arene.coords(self.dessin_robot, self.robot.x, self.robot.y, self.robot.x + self.robot.width, self.robot.y + self.robot.height)
        self.after_id = self.arene.after(50, self.update)
    
    def outil_crayon(self):
        """
        Crayon pour un robot
        """
        self.arene.create_line(self.robot.x, self.robot.y, self.robot.x + 1, self.robot.y + 1, fill='green', width=3)


        
    def tracer_carre(self):
        """
        Pour faire "dessiner" un carré à un objet. (Fonction qui est censée être dans le module controleur)
        """

        # Déplacement sur le côté haut (vers la droite)
        if (self.cpt < 50):
            self.robot.change_dir(1, 0)#on change la direction ici
            self.robot.x += self.robot.dir[0]
            self.robot.y += self.robot.dir[1]
            self.outil_crayon()
            self.cpt += 1
            print(self.cpt)
        
        # Déplacement sur le côté droit (vers le bas)
        if (50 <= self.cpt) and (self.cpt < 100):
            self.robot.change_dir(0, 1)
            self.robot.x += self.robot.dir[0]
            self.robot.y += self.robot.dir[1]
            self.outil_crayon()
            self.cpt += 1
        
        # Déplacement sur le côté bas (vers la gauche)
        if (100 <= self.cpt) and (self.cpt < 150):
            self.robot.change_dir(-1, 0)
            self.robot.x += self.robot.dir[0]
            self.robot.y += self.robot.dir[1]
            self.outil_crayon()
            self.cpt += 1

        # Déplacement sur le côté gauche (vers le haut)
        if (150 <= self.cpt) and (self.cpt < 200):
            self.robot.change_dir(0, -1)
            self.robot.x += self.robot.dir[0]
            self.robot.y += self.robot.dir[1]
            self.outil_crayon()
            self.cpt += 1

        
        self.after_id2 = self.arene.after(50, self.tracer_carre)
    
    def run(self):
        """
        Permet de faire tourner la simulation comme on le souhaite
        """
        self.tracer_carre()
        self.update()
        # Permet de redessiner le terrain après un certain nombre de millisecondes
    
    def stop(self):
       """
       Arrête la simulation
       """
       if self.after_id:
           self.arene.after_cancel(self.after_id)
           self.after_id = None


fausse_arene = Arene_tmp(600, 600)
wall_e = Sim(200, 200)
simulation = Tk()
Viewer(simulation, wall_e, fausse_arene)
simulation.mainloop()