from tkinter import *
from tkinter import ttk


class Viewer :

    def __init__(self, simulation) : # + param arene ?

        simulation.title("Gopigo Simulator")
        simulation.columnconfigure(0, weight = 1)
        simulation.rowconfigure(0, weight = 1)
        
        io = ttk.Frame(simulation)
        terrain = Canvas(io, borderwidth = 2, relief = 'ridge', width = 600, height = 600, background = "white")
        
        play = ttk.Button(io, text = "Play")
        stop = ttk.Button(io, text = "Stop")

        io.grid(column = 0, row = 0, sticky = (N, S, E, W))
        terrain.grid(column = 0, row = 0, columnspan = 6, rowspan = 6, sticky = (N, S, E, W))
        play.grid(column = 6, row = 3, sticky = (W, E))
        stop.grid(column = 8, row = 3, sticky = (W, E))

        for i in range(6) :
            io.columnconfigure(i, weight = 5)
        for i in range(6, 9) :
            io.columnconfigure(i, weight = 1)
        for i in range(6) :
            io.rowconfigure(i, weight = 1)
        
        terrain.create_rectangle(100, 50, 300, 250, fill = 'red', outline = 'red')
        

simulation = Tk()
Viewer(simulation)
simulation.mainloop()