import unittest
from modele.arene import Obstacle

class TestObstacle(unittest.TestCase):

    def test_obstacle_is_created(self):
        obstacle = Obstacle()
        self.assertIsInstance(obstacle, Obstacle)

if __name__ =='__main__':
    unittest.main()