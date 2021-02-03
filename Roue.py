class Roue(object):
    def __init__(self):
        self.__moteurAllume=False
        self.__vitesseRotation=0.
    def setVitesseRotation(self,vitesse):
        """
        float
        Permet de changer la vitesse du moteur
        """
        self.__vitesseRotation=vitesse
        if vitesse==0. :
            self.__moteurAllume=False
        else:
            self.__moteurAllume=True
    def get_moteurAllume(self):
        """"
        Retourne la valeur de moteurAllume
        """
        return self.__moteurAllume
    def get_vitesseRotation(self):
        """
        Retourne la valeur de vitesseRotation
        """
        return self.__vitesseRotation

    