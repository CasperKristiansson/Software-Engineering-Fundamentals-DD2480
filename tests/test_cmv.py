import unittest
import sys
import os

# Add root folder to current path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

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
        
    def test_condition7(self):

        """
        Test cases for the condition7 method.

        Test scenarios:
        1. Assert that True is returned with normal input
        2. Assert that False is returned if dist is less than LENGTH1
        3. Assert that False is returned if POINTS is empty
        4. Assert that False is returned if POINTS has less than 3 points
        5. Assert that False is returned if dist equals to LENGTH1

        Parameters:
        - self: the TestCase object

        Returns:
        None
         """

        filename = "cmv_cond3.in"

        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        self.assertTrue(cmv.condition7(), "At least one set of points, separated by K_PTS with a distance greater than LENGTH1")

        cmv.LENGTH1 = 100000
        self.assertFalse(cmv.condition7(), "If distance is shorter than LENGTH1, the method should return False")

        cmv.NUMPOINTS = 0
        cmv.POINTS = []
        self.assertFalse(cmv.condition7(), "If POINTS is empty, the method should return False")

        cmv.NUMPOINTS = 2
        cmv.POINTS = [(1.321, -2.540), (-2.432, 4.392)]
        self.assertFalse(cmv.condition7(), "If POINTS does not contain at least 3 points, the method should return False")

        cmv.POINTS = [(1, 1), (2, 2), (5, 5), (10, 10)]
        cmv.NUMPOINTS = 4
        cmv.K_PTS = 1
        cmv.LENGTH1 = 11.313708498984761
        self.assertFalse(cmv.condition7(), "The distance need to be greater than LENGTH1, not equal or greater than LENGTH1")


