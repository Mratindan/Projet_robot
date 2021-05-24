import unittest
from outils import Point, Vecteur

class TestOutilsMathematiques(unittest.TestCase):

    def setUp(self):
        self.test_case_distance = [
            (Point(1, 2), Point(4, 6), 5.0)
        ]

        self.test_case_addition = [
            (Vecteur(Point(-3, 0), Point(0, 4)), Vecteur(Point(-1, 0), Point(0, 5)), Vecteur(Point(-4, 0), Point(0, 9)))
        ]

    def test_distance(self):
        for case in self.test_case_distance:
            point = case[1]
            self.assertEqual(point.distance(case[0]), case[2])

    def test_addition(self):
        for case in self.test_case_addition:
            vecteur = case[1]
            self.assertEquals(vecteur.addition(case[0]), case[2])

if __name__ == '__main__':
    unittest.main()