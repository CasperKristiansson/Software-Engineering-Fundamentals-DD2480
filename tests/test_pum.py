import math
import unittest
import sys
import os

# Add root folder to current path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.pum import create_pum
from src.cmv import CMV
from src.parse import read_input_to_dict

class TestPUM(unittest.TestCase):

    def instantiate_object(self, filepath):
        """
            Creates an object of the CMV class for testing

            Parameters:
            - Absolute path to file containing the input data

            Returns:
            - CMV object
        """
        d = read_input_to_dict(filepath)
        return CMV(d)
                 
    def test_pum_example(self):
        """
        Test case for the creation of the PUM matrix. The input data is from the 
        example found in the DECIDE program specification.
        """

        cmv = CMV({})

        cmv.CMV_VECTOR = [False, True, True, True, False, False, False, False, False, False, False, False, False, False, False]
        cmv.LCM = [
            ["ANDD", "ANDD", "ORR", "ANDD", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"],
            ["ANDD", "ANDD", "ORR", "ORR", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"], 
            ["ORR", "ORR", "ANDD", "ANDD", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"], 
            ["ANDD", "ORR", "ANDD", "ANDD", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"],
            ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"],
            ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"],
            ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"],
            ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"],
            ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"],
            ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"],
            ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"],
            ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"],
            ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"],
            ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"],
            ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"]
        ] 
        
        expected_pum = [
            [None, False, True, False, True, True, True, True, True, True, True, True, True, True, True],
            [False, None, True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, None, True, True, True, True, True, True, True, True, True, True, True, True],
            [False, True, True, None, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, None, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, None, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, None, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, None, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, None, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, None, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, None, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, None, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, None, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True, None, True],  
            [True, True, True, True, True, True, True, True, True, True, True, True, True, True, None]
        ]

        actual_pum = create_pum(cmv)

        self.assertEqual(expected_pum, actual_pum)