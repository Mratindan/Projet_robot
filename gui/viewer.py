from tkinter import *
from tkinter import ttk


class Viewer :

    def __init__(self, simulation) :

        # Création de la fenêtre principale de l'application
        simulation.title("Gopigo Simulator")
        # columnconfigure et rowconfigure pour permettre à la fenêtre de s'adapter si l'utilisateur resize 
        simulation.columnconfigure(0, weight = 1)
        simulation.rowconfigure(0, weight = 1)
        
        # Création des widgets :
        # Le cadre principale qui contiendra la toile, les boutons etc
        cadre = ttk.Frame(simulation)
        # La toile dans laquelle sera dessinée la simulation
        terrain = Canvas(cadre, borderwidth = 2, relief = 'ridge', width = 600, height = 600, background = "white")
        # Les boutons
        play = ttk.Button(cadre, text = "Play")
        stop = ttk.Button(cadre, text = "Stop")

        # Placement des widgets
        cadre.grid(column = 0, row = 0, sticky = (N, S, E, W))
        terrain.grid(column = 0, row = 0, columnspan = 6, rowspan = 6, sticky = (N, S, E, W))
        play.grid(column = 6, row = 3, sticky = (W, E))
        stop.grid(column = 8, row = 3, sticky = (W, E))

        # Pour déterminer le comportement du cadre lors des resize
        for i in range(6) :
            cadre.columnconfigure(i, weight = 5)
        for i in range(6, 9) :
            cadre.columnconfigure(i, weight = 1)
        for i in range(6) :
            cadre.rowconfigure(i, weight = 1)
        
        terrain.create_rectangle(100, 50, 300, 250, fill = 'red', outline = 'red')
        

simulation = Tk()
Viewer(simulation)
simulation.mainloop()