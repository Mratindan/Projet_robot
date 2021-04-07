import unittest

from Projet_robot.modele.Robot import Robot

class TestRobot(unittest.TestCase):
    def setUp(self):
        r = Robot(1, 1)

    def affiche_Position(self):
        print(self.Robot.affichePosition())
    def change_position(self):
        self.r.changePosition(9, 30, 0)
        print("x= ")
        self.r.positionVecteur.point1.affichePolynome('t')
        print("y= ")
        self.r.positionVecteur.point2.affichePolynome('t')
        self.r.changePosition(7,80,5)
        print("x= ")
        self.r.positionVecteur.point1.affichePolynome('t')
        print("y= ")
        self.r.positionVecteur.point2.affichePolynome('t')

        self.assertEqual(self.r,self.r.changePosition)
if __name__=='__main__':
    unittest.main()