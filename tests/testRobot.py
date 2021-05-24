import unittest

from modele import Robot_simple


class TestRobot(unittest.TestCase):

    def setUp(self):
        self.test_case_se_deplacer = [
            (Robot_simple(1,1))
        ]

    def test_se_deplacer(self):
        for case in self.test_case_se_deplacer:
            robot = Robot_simple(1,1)
            robot.set_v_roue_gauche(1)
            robot.set_v_roue_droite(3)
            with self.assertRaises(Exception):
                robot.se_deplacer()

if __name__=='__main__':
    unittest.main()