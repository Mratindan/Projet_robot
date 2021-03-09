from tkinter import *
from tkinter import ttk
import time
import threading

class Controleur_carre(threading.Thread):
    """
    Le controleur qui permet au robot de faire un carré, en attendant qu'il y ait les import nécessaires pour utiliser les fichiers du module controleur ici.
    """

    def __init__(self, robot):
        threading.Thread.__init__(self)
        self.robot = robot
        self.cpt = 0
        self.done = False 


    def update_step(self):
        self.cpt += 1            


    def tracer_carre(self):
        """
        Pour faire "dessiner" un carré à un robot.
        """

        # Déplacement sur le côté haut (vers la droite)
        if (self.cpt < 50):
            self.robot.change_dir(1, 0)#on change la direction ici
            self.robot.crayon = True
            
        # Déplacement sur le côté droit (vers le bas)
        if (50 <= self.cpt) and (self.cpt < 100):
            self.robot.change_dir(0, 1)
            self.robot.crayon = True
        
        # Déplacement sur le côté bas (vers la gauche)
        if (100 <= self.cpt) and (self.cpt < 150):
            self.robot.change_dir(-1, 0)
            self.robot.crayon = True

        # Déplacement sur le côté gauche (vers le haut)
        if (150 <= self.cpt) and (self.cpt < 200):
            self.robot.change_dir(0, -1)
            self.robot.crayon = True

        if (self.cpt >= 200):
            self.robot.change_dir(0, 0)
            self.robot.crayon = False
            self.done = True


    def run(self):       
        while True:
            print("cpt = ", self.cpt)
            self.tracer_carre()
            self.update_step()
            time.sleep(0.1)
            if self.done:
                break


class Robot_tmp :
    def __init__(self, x, y):
        """ 
        Représente un robot avec une position initiale (x, y) 
        """
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.dir = [0, 0]
        self.crayon = False # Définit si le robot utilise un crayon ou pas
    
    def change_dir(self, dx, dy):
        """
        Permet de changer la direction du robot
        """
        self.dir[0] = dx
        self.dir[1] = dy
    
    def se_deplacer(self):
        """
        Permet au robot de se déplacer
        """
        self.x += self.dir[0]
        self.y += self.dir[1]


class Arene_tmp(threading.Thread) :
    """
    Le modèle de l'arène, en attendant qu'il y ait les import nécessaires pour utiliser un objet arene ici. 
    """

    def __init__(self, width, height, robot, controleur):
        threading.Thread.__init__(self)
        self.width = width
        self.height = height
        self.robot = robot
        self.controleur = controleur

    def update(self):
        """
        Met à jour le modèle
        """
        self.robot.se_deplacer()
    
    def run(self):
        while True:
            print("Controleur de l'arene")
            self.update()
            time.sleep(0.1)
            if self.controleur.done:
                break


class Viewer :

    def __init__(self, arene):
        """
        simulation : Tk
        Initialise une fenêtre graphique 
        """

        self.simulation = Tk()

        # Variables nécessaires pour faire tourner la simulation
        self.after_id = None
        self.arene = arene
        self.robot = self.arene.robot

        # Nommage de la fenêtre principale de l'application
        self.simulation.title("Gopigo Simulator")
        # Détermination du comportement de la fenêtre lors des resize
        self.simulation.columnconfigure(0, weight = 1)
        self.simulation.rowconfigure(0, weight = 1)
        
        # Création des widgets :
        # Le cadre principale qui contiendra la toile, les boutons etc
        self.cadre = ttk.Frame(self.simulation)
        # La toile dans laquelle sera dessinée la simulation
        self.dessin_arene = Canvas(self.cadre, borderwidth = 2, relief = 'ridge', width = self.arene.width, height = self.arene.height, background = "white")
        # Les boutons
        self.play = ttk.Button(self.cadre, text = "Play", command = self.run)
        self.stop = ttk.Button(self.cadre, text = "Stop", command = self.stop)
        # Association de certaines touches du clavier à des commandes (en alternative aux boutons)
        self.simulation.bind("<Return>", lambda e: self.play.invoke())
        self.simulation.bind("<space>", lambda e: self.stop.invoke())

        # Placement des widgets
        self.cadre.grid(column = 0, row = 0, sticky = (N, S, E, W))
        self.dessin_arene.grid(column = 0, row = 0, columnspan = 6, rowspan = 6, sticky = (N, S, E, W))
        self.play.grid(column = 6, row = 3, sticky = (W, E))
        self.stop.grid(column = 8, row = 3, sticky = (W, E))

        # Détermination du comportement du cadre lors des resize
        for i in range(6):
            self.cadre.columnconfigure(i, weight = 5)
            self.cadre.rowconfigure(i, weight = 1)
        for i in range(6, 9):
            self.cadre.columnconfigure(i, weight = 1)

        # Initialisation des dessins du robot et des obstacles 
        self.dessin_robot = self.dessin_arene.create_rectangle(self.robot.x, self.robot.y, self.robot.x + self.robot.width, self.robot.y + self.robot.height, fill = 'red', outline = 'red')
        #self.dessiner_obstacles
    
    def dessiner_obstacles():
        """
        Dessine les obstacles à partir de la liste self.arene.list_obstacles
        """
    
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
        self.dessin_arene.coords(self.dessin_robot, self.robot.x, self.robot.y, self.robot.x + self.robot.width, self.robot.y + self.robot.height)
        self.after_id = self.dessin_arene.after(50, self.update)

    
    def run(self):
        """
        Démarre la simulation
        """
        self.update()

    def start(self):
        """
        Lance l'interface graphique de la simulation
        """
        self.run()
        self.simulation.mainloop()
    
    def stop(self):
       """
       Arrête la simulation
       """
       if self.after_id:
           self.dessin_arene.after_cancel(self.after_id)
           self.after_id = None


# Notre robot
wall_e = Robot_tmp(200, 200)

# Controleur
ctrl = Controleur_carre(wall_e)

# Arene
arene = Arene_tmp(600, 600, wall_e, ctrl)

# Viewer
interface_graphique = Viewer(arene)

# Démarrage des threads
ctrl.start()
arene.start()
interface_graphique.start()
