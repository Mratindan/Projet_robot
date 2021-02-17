import unittest
import sys
sys.path.append("..")
from Projet_robot.Arene import Arene
from Projet_robot.Point import Point

class TestArene(unittest.TestCase):
    def test_arene_is_created(self):
        arene = Arene(10,15)
        self.assertIsInstance(arene,Arene)


if __name__ =='__main__':
    unittest.main()
