import unittest
from modele import Polynome

class TestPolynome(unittest.TestCase):

    def setUp(self):
        self.test_case_calcul = [
            (2, Polynome(2,2,1), 13),
            (2, Polynome(-1,3,1), 3),
            (2, Polynome(0,0,0), 0),
            (0, Polynome(-1,3,1), 1)
        ]

    def test_calcul(self):
        for case in self.test_case_calcul:
            polynome = case[1]
            self.assertEquals(polynome.calcul(case[0]),case[2])

if __name__ =='__main__':
    unittest.main()