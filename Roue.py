class Roue(object):

    def __init__(self):
        self.moteurAllume=False
        self.vitesseRotation=0.

    def setVitesseRotation(self,vitesse):
        """
        float --> None
        Permet de changer la vitesse du moteur
        """
        self.vitesseRotation=vitesse
        if vitesse==0. :
            self.moteurAllume=False
        else:
            self.moteurAllume=True

    def get_moteurAllume(self):
        """"
        None -> boolean
        Retourne la valeur de moteurAllume
        """
        return self.moteurAllume

    def get_vitesseRotation(self):
        """
        None -> float
        Retourne la valeur de vitesseRotation
        """
        return self.vitesseRotation

    