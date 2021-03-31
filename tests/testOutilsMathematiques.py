import unittest
from Projet_robot-main.outils import outils_mathematiques


class TestOutilsMathematiques(unittest.TestCase):
    def setUp(self):
        self.point1 = outils_mathematiques(1, 2)
        self.point2 = outils_mathematiques(4, 6)
        self.point3 = outils_mathematiques(-2, -1)
        self.point4 = outils_mathematiques(6, -3)

        self.v1 = outils_mathematiques(self.point1, self.point2)
        self.v2 = outils_mathematiques(self.point3, self.point4)
        self.v3 = outils_mathematiques(-3, 4)
        self.v4 = outils_mathematiques(-1, 5)
        self.v5 = outils_mathematiques(1, 2)

        self.vecteurTestAngle1 = outils_mathematiques(4, 1)
        self.vecteurTestAngle2 = outils_mathematiques(4, -2)

    def test_distance(self):
        self.assertIsNot(self.point1.distance(self.point2), self.point3.distance(self.point4))
        self.assertIs(self.point1.distance(self.point2), self.point2.distance(
            self.point1))  #erreur: AssertionError: 5.0 is not 5.0 (!!)or: 5.0 is not 5.0 (!!)

    def test_norme(self):
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

    def test_produitScalaire(self):

    def test_calculAngle(self):
        self.assertEqual(self.v1.calculAngle(self.v2), self.vecteurTestAngle1.calculAngle(self.vecteurTestAngle2))

if __name__ == '__main__':
    unittest.main()