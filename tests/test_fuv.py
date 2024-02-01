import unittest
import sys
import os


# Add root folder to current path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.fuv import generate_fuv

class Test_FUV(unittest.TestCase):

    def test_correct_behavior_puv_1(self):
        """
        Test if all elements in FUV is True, when all elements in PUV is false

        Parameters:
        - self: The instance of the test class.
            
        Returns:
        - None
        """
        puv = [False]*15
        pum = [[False] * 15 for _ in range(15)]
        self.assertTrue(all(generate_fuv(pum, puv)))

    def test_correct_behavior_puv_2(self):
        """
        Test if all in FUV contains one False when PUV contains one true and the index of that element is False in the PUM

        Parameters:
        - self: The instance of the test class.
            
        Returns:
        - None
        """
        puv = [False]*15
        puv[13] = True
        pum = [[False] * 15 for _ in range(15)]
        self.assertFalse(all(generate_fuv(pum, puv)))

    def test_correct_behavior_PUM_1(self):
        """
        Test if all elements in FUV is True, when all elements in PUM is True
        and all elements in PUV is True

        Parameters:
        - self: The instance of the test class.
            
        Returns:
        - None
        """
        puv = [True]*15
        pum = [[True] * 15 for _ in range(15)]
        self.assertTrue(all(generate_fuv(pum, puv)))
        
    def test_correct_behavior_PUM_2(self):
        """
        Test if some elements in FUV is False, when some elements in PUM is False
        and all elements in PUV is True

        Parameters:
        - self: The instance of the test class.
            
        Returns:
        - None
        """
        puv = [True]*15
        pum = [[True] * 15 for _ in range(15)]
        pum[3][6] = False
        self.assertFalse(all(generate_fuv(pum, puv)))

    