import unittest

from Projet_robot.Vecteur import Vecteur
from Projet_robot.Point import Point


class TestVecteur(unittest.TestCase):
    def setUp(self):
        self.v1 = Vecteur(2, 5)
        self.v2 = Vecteur(4, 7)


    def test_est_egal(self):
        self.assert_(self.v1.estEgal(self.v2))





if __name__ =='__main__':
    unittest.main()







print("Produit scalaire entre vecteurs 1 et 2 : ", v3.produitScalaire(v4))
print("Produit scalaire entre vecteurs 3 et 4 : ", v1.produitScalaire(v2))







#print("point1 de v : (", v.point1.x, ",", v.point1.y, ")")
#print("point2 de v : (", v.point2.x, ",", v.point2.y, ")")
#print("PS entre v1 et v2 : ", v1.produitScalaire(v2,30))