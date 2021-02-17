import unittest

from Projet_robot.Point import Point

class TestPoint (unittest.TestCase):
    def setUp(self):
        self.p1 = Point(1,2)
        self.p2 = Point(4,6)
        self.p3 = Point(-2, -1)
        self.p4 = Point(6, -3)

    def test_point_cree(self):
        self.assertIsInstance(self.p1,Point)
        self.assertIsInstance(self.p2,Point)

    def test_methode_distance(self):
        self.assert_(True,"ok")

    def test_distance(self):
        self.assertEqual(self.p1.distance(self.p2),self.p3.distance(self.p4))


if __name__ =='__main__':
    unittest.main()


