from math import fabs
import sys
import unittest
import time
import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../modele'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
from modele.arene import Arene
class TestArene(unittest.TestCase):
    def setUp(self):
        self.test_case_est_exterieur_mur = [
            (-1,5,Arene(30,15), True), 
            (0,0,Arene(30,15),False), 
            (5,-1,Arene(30,15),True),
            (5,5,Arene(4,10),True),
            (5,5,Arene(10,4),True),
            (5,10,Arene(4,9),True),
            (5,5,Arene(10,10),True)]                          

    def test_est_exterieur_mur(self): 
        for case in self.test_case_est_exterieur_mur:
            arene = case[2]
            self.assertEquals(arene.est_exterieur_mur(case[0],case[1]), case[3])
            
if __name__ =='__main__':
    unittest.main()
