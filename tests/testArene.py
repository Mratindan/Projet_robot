# -*- coding: utf-8 -*-
import unittest
from modele import Robot
from modele.arene import Arene

class TestArene(unittest.TestCase):

    def setUp(self):
        self.test_case_est_exterieur_mur = [
            (-1,5,Arene(30,15,Robot(200, 300),None,10,10),True),
            (0,0,Arene(30,15,Robot(200, 300),None,10,10),False),
            (5,-1,Arene(30,15,Robot(200, 300),None,10,10),True),
            (5,5,Arene(30,15,Robot(200, 300),None,10,10),False),
            (5,10,Arene(30,15,Robot(200, 300),None,10,10),False),
            (5,5,Arene(30,15,Robot(200, 300),None,10,10),False)]

    def test_est_exterieur_mur(self): 
        for case in self.test_case_est_exterieur_mur:
            arene = case[2]
            self.assertEquals(arene.est_exterieur_mur(case[0],case[1]), case[3])
            
if __name__ =='__main__':
    unittest.main()
