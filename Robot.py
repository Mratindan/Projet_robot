class Robot :
    "Definition d'un robot"
    
    def __init__(self,a,b):
        print("Creation d'un robot")
        self.__x = a
        self.__y = b
        self.__direction = 0.
        self.__vitesse = 0.
        self.__acceleration = 0.
        
    def deplace(self, dx, dy):
        """
        int,int
        Deplace le robot de dx en abscisse et dy en ordonne
        """
        self.__x = self.__x + dx
        self.__y = self.__y + dy
        print("Le tobot s'est déplacé en [",self.__x,",",self.__y,"]")
        
    def affichePosition(self):
        """
        Affiche la position du tobot.
        """
        print("Position du tobot [",self.__x,",",self.__y,"]")
            
            
    def setVitesse(self,newVitesse):
        """
        float
        Change la vitessee du robot
        """
        self.__vitesse = newVitesse

    def setDirection(self,newDirection):
        """
        float
        Change la direction du robot
        """
        self.__direction = newDirection
        
    def setX(self,newX):
        """
        int
        Change l'abscisse du robot
        """
        self.__x = newX
        
    def setY(self,newY):
        """
        int
        Change l'Ordonne du robot
        """
        self.__y = newY
        
    def getRobotAbscisse(self):
        """"
        Retourne la valeur de x
        """
        return self.__x
    
    def getRobotOrdonne(self):
        """"
        Retourne la valeur de y
        """
        return self.__y
    
    def getVitesse(self):
        """
        Retourne la vitesse du robot
        """
        return self.__vitesse

    def getVitesse(self):
        """
        Retourne la direction du robot
        """
        return self.__direction