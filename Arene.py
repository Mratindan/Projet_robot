import time
class Arene:
    "Terrain sur lequel peut évoluer un robot et des objets quelconques"

    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.terrain = [[' '] * largeur for i in range(hauteur)]
        self.listeObstacles = []
        self.robot = None 

    def afficherArene(self):
        """
        None -> None
        Permet d'afficher l'état actuel du terrain
        """
        largeur_bord = self.largeur + 2

        # Bord du haut
        for k in range(largeur_bord):
            print("#", end = '')
        print("")

        # Terrain en lui-même et bord sur les côtés
        for i in range(self.hauteur):
            print("#", end = '')
            for j in range(self.largeur):
                print(self.terrain[i][j], end = '')
            print("#")
        
        # Bord du bas
        for k in range(largeur_bord):
            print("#", end = '')
        print("")

    def estVide(self, pos_largeur, pos_hauteur):
        """
        int * int -> boolean
        Renvoie true si une case est vide et false sinon
        """
        if (0 > pos_largeur) or (self.largeur < pos_largeur) or (0 > pos_hauteur) or (self.hauteur < pos_hauteur) :
            print("estVide : cette case n'est pas accessible")
            return None 
        return self.terrain[pos_largeur][pos_hauteur] == ' '

    #def placerRobot(self):
    #   self.terrain[self.robot.x][self.robot.y] = "R"

    def placerObstacle(self, posLargeur, posHauteur):
        """
        int * int
        Permet de placer un obstacle dans l'arène
        """
        if arene.estVide(posLargeur,posHauteur):
            self.terrain[posLargeur][posHauteur] = 'O'
        else:
            print("La case est deja occupee, impossible de placer quoi que ce soit en ({},{})".format(posLargeur,posHauteur))
            self.terrain[posLargeur][posHauteur] = 'O'
            return

    def supprimerObstacle(self, posLargeur, posHauteur):
        """
        int * int
        Permet de retirer un obstacle present dans l'arène
        """
        if not(arene.estVide(posLargeur,posHauteur)) and (arene.terrain[posLargeur][posHauteur] == 'O'):
            self.terrain[posLargeur][posHauteur] = ' '
        else:
            print("La position donnee ({},{}) est deja vide.".format(posLargeur,posHauteur))
            return

    """def ajouterObstacle(self, posLargeur, posHauteur):
                    
                    int * int
                    #Permet d'ajouter un obstacle
                    
                    if arene.estVide(posLargeur,posHauteur):
                        listeObstacles.append(Obstacle())
                        placerObstacle(posLargeur,posHauteur)"""
            



# Test rapide   
arene = Arene(30, 15)
arene.afficherArene()
print("Placons un obstacle en (10,10)")
arene.placerObstacle(10,10)
arene.afficherArene()
print("Essayons de placer un autre obstacle en (10,10)")
arene.placerObstacle(10,10)
time.sleep(5)

print("Supprimons maintenant l'obstacle que nous venons de creer")
arene.supprimerObstacle(10,10)
arene.afficherArene()
print("Essayons de le supprimer a nouveau")
arene.supprimerObstacle(10,10)
arene.afficherArene()


"""if arene.estVide(1, 0):
    print("La case est vide")
else:
    print("La case n'est pas vide")


if arene.estVide(20, 30):
    print("La case est vide")
else:
    print("La case n'est pas vide")"""
            

