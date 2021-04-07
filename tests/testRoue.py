import unittest
from Projet_robot.modele.Roue import Roue

class TestRoue(unittest.TestCase):

    def setUp(self):
        self.roue = Roue()

    def test_arene_is_created(self):
            self.assertIsInstance(self.roue, Roue)

if __name__ =='__main__':
    unittest.main()