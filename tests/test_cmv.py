import unittest
import sys
import os

# Add root folder to current path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.cmv import CMV
from src.parse import read_input_to_dict

class TestCMV(unittest.TestCase):

    # Run before each test
    def instantiate_object(self, filepath):
        d = read_input_to_dict(filepath)
        return CMV(d)

    # Placeholder functions - Most likely need more than one test per function

    def test_construct_vector(self):
        filename = ""
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO

    def test_condition0(self):
        filename = ""
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO

    def test_condition1(self):
        filename = ""
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO

    def test_condition2(self):
        filename = ""
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO

    def test_condition3(self):
        filename = ""
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO

    def test_condition4(self):
        filename = ""
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO

    def test_condition5(self):
        filename = ""
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO

    def test_condition6(self):
        filename = ""
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO

    def test_condition7(self):
        filename = ""
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO

    def test_condition8(self):
        filename = ""
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO

    def test_condition9(self):
        filename = ""
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO

    def test_condition10(self):
        filename = ""
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO

    def test_condition11(self):
        filename = ""
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO

    def test_condition12(self):
        filename = ""
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO

    def test_condition13(self):
        filename = ""
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO

    def test_condition14(self):
        filename = ""
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        #TODO