import unittest

from Projet_robot.Arene import Arene

class TestArene(unittest.TestCase):
    def test_arene_is_created(self):
        arene = Arene(10,15)
        self.assertIsInstance(arene,Arene)

    def test_est_vide(self):
        self.assert_(True,"est vide")


if __name__ =='__main__':
    unittest.main()




