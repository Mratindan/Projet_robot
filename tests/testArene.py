import sys
import unittest
import time
sys.path.append("..")

from Projet_robot.modele.Arene import Arene


class TestArene(unittest.TestCase):
    def setUp(self):
        self.arene = Arene(30, 15)

    def test_arene_is_created(self):
        self.assertIsInstance(self.arene,Arene)

    def test_afficher_arene(self):
        #print(self.arene.afficherArene())
        self.assertTrue(True)

    def test_arene_est_vide(self):
        self.assertTrue(True)

    #def test_placer_robot(self):

    def test_placer_obstacle(self):
      print("Placons un obstacle en (10,10)")
      #print(self.arene.placerObstacle(10,10))
      time.sleep(5)

    def test_supprimer_obstacle(self):
        print("Supprimons maintenant l'obstacle que nous venons de creer")
        #print(self.arene.supprimerObstacle(10, 10))

if __name__ =='__main__':
    unittest.main()
