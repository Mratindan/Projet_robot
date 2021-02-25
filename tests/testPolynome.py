import unittest
from Projet_robot.modele.Polynome import Polynome

class TestPolynome(unittest.TestCase):
    def setUp(self):
        self.polynome = Polynome(2,4,6)
    def test_calcul(self):
        self.assertEqual(self.polynome.calcul(2),22)
if __name__ =='__main__':
    unittest.main()