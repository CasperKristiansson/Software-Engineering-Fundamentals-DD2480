import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.utils import area_of_triangle


class TestCMV(unittest.TestCase):
    def test_area_of_triangle(self):
        """
            Test the area_of_triangle function from utils.py

            1. Test a triangle with vertices (0, 0), (3, 0), (0, 4)
            2. Test a triangle where the points are in a line
            3. Test a triangle where vertices with negative coordinates
            4. Test a triangle where vertices with float coordinates
        """

        self.assertAlmostEqual(area_of_triangle((0, 0), (3, 0), (0, 4)), 6.0)

        self.assertEqual(area_of_triangle((0, 0), (1, 1), (2, 2)), 0.0)

        self.assertAlmostEqual(area_of_triangle((-1, 0), (0, -1), (-1, -1)), 0.5)

        self.assertAlmostEqual(area_of_triangle((0.5, 0.5), (1.5, 0.5), (0.5, 1.5)), 0.5)


if __name__ == '__main__':
    unittest.main()
