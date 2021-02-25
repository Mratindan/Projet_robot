import unittest

from Projet_robot.outils.Point import Point

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point1 = Point(1, 2)
        self.point2 = Point(4, 6)
        self.point3 = Point(-2, -1)
        self.point4 = Point(6, -3)

    def test_distance(self):
        self.assertIsNot(self.point1.distance(self.point2),self.point3.distance(self.point4))
        print("Distance entre les points (1,2) et (4,6) = ", self.point1.distance(self.point2))
        print("Distance entre les points (-2,-1) et (6,-3) = ", self.point4.distance(self.point3))
        self.assertIs(self.point1.distance(self.point2),self.point2.distance(self.point1))#erreur: AssertionError: 5.0 is not 5.0 (!!)

if __name__=='__main__':
    unittest.main()
