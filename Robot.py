class Robot :
    "Definition d'un robot"
    
    def __init__(self, a, b):
        print("Creation d'un robot")
        self.position = Point(a, b)
        self.direction = 0.
        self.vitesse = 0.
        self.acceleration = 0.
        
    def deplace(self, dx, dy):
        """
        int * int --> None
        Déplace le robot de dx en abscisse et dy en ordonnée.
        """
        self.position.x += dx
        self.position.y += dy
        print("Le robot s'est deplace en [", self.position.x, ",", self.position.y, "]")
        
    def affichePosition(self):
        """
        None --> None
        Affiche la position du robot.
        """
        print("Position du robot [", self.position.x, ",", self.position.y, "]")
            

