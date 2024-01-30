import unittest
import sys
import os

# Add root folder to current path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.fuv import FUV

class TestFUV(unittest.TestCase):

    # Run before each test
    def instantiate_object(self, filepath):
        d = {}

        with open(filepath, "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                d[key] = value
        
        file.close()

        return FUV(d)

    # Placeholder functions - Most likely need more than one test per function

    def test_some_function(self):
        filename = ""
        fuv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO
