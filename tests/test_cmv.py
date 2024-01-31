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
