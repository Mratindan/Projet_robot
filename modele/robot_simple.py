

class Robot_simple :
    def __init__(self, x, y):
        """ 
        Représente un robot avec une position initiale (x, y) 
        """
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
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