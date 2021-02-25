import unittest

from Projet_robot.outils.Vecteur import Vecteur
from Projet_robot.outils.Point import Point

class TestVecteur(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(4, 1)
        self.p2 = Point(0, 0)
        self.p3 = Point(4, -2)
        self.p4 = Point(0, 0)

        self.v1 = Vecteur(self.p1, self.p2)
        self.v2 = Vecteur(self.p3, self.p4)
        self.v3 = Vecteur(-3, 4)
        self.v4 = Vecteur(-1, 5)
        self.v5 = Vecteur(1, 2)

        self.vecteurTestAngle1 = Vecteur(4, 1)
        self.vecteurTestAngle2 = Vecteur(4, -2)

        print("p1 : (", self.p1.x, ",", self.p1.y, ")")
        print("p2 : (", self.p2.x, ",", self.p2.y, ")")
        print("p3 : (", self.p3.x, ",", self.p3.y, ")")
        print("p4 : (", self.p4.x, ",", self.p4.y, ")")

    def test_norme(self):
        print("Norme de v1 : ", self.v1.calculNorme())
        print("Norme de v2 : ", self.v2.calculNorme())
        self.assertNotEqual(self.v1.calculNorme(),self.v2.calculNorme())

    def test_clonage(self):
        self.assertTrue(True)

    def test_rotation(self):
        self.assertTrue(True)

    def test_est_egal(self):
        self.assertNotEqual(self.v1,self.v2)

    def test_addition(self):
        self.assertTrue(True)

    def test_produitVectoriel(self):
        print("Produit vectoriel entre vecteurs 1 et 2 : ", self.v1.produitVectoriel(self.v2))

    def test_produitScalaire(self):
        print("Produit scalaire entre vecteurs 3 et 4 : ", self.v3.produitScalaire(self.v4))
        print("Produit scalaire entre vecteurs 1 et 2 : ", self.v1.produitScalaire(self.v2))


    def test_calculAngle(self):
        print("Angle (cosinus) entre v1 et v2 : ", self.v1.calculAngle(self.v2))
        print("Angle entre vecteurs tests ", self.vecteurTestAngle1.calculAngle(self.vecteurTestAngle2))
        self.assertEqual(self.v1.calculAngle(self.v2), self.vecteurTestAngle1.calculAngle(self.vecteurTestAngle2))

if __name__ == '__main__':
    unittest.main()