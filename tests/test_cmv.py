import unittest
import sys
import os

# Add root folder to current path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.cmv import CMV
from src.parse import read_input_to_dict

class TestCMV(unittest.TestCase):

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
    
    def test_condition6(self):
        """
        Test the condition6 method of the CMV class.

        This method checks the behavior of the condition6 method under various scenarios:
        1. An instance where the requirement is fulfilled
        2. An instance where the requirement is not fulfilled
        3. An instance where the list is too short
        4. An instance where the first and last points coincide, where the requirement is still fulfilled
        5. An instance where the first and last points coincide, but where the requirement is not fulfilled
        
        Parameters:
        - self: The instance of the test class.
        
        Returns:
        - None
        """
        filename="condition6/cmv_cond6_accept.in"

        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        self.assertTrue(cmv.condition6())

        filename="condition6/cmv_cond6_reject.in"
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        self.assertFalse(cmv.condition6())

        cmv.NUMPOINTS = 2
        self.assertFalse(cmv.condition6())

        filename="condition6/cmv_cond6_identical_points_accept.in"
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        self.assertTrue(cmv.condition6())

        filename="condition6/cmv_cond6_identical_points_reject.in"
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        self.assertFalse(cmv.condition6())


        






