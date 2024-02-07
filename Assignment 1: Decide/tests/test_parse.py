import unittest
import sys
import os


# Add root folder to current path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import src.parse as p

class Test_Parse(unittest.TestCase):
    
    # Run before each test
    def instantiate_object(self, filepath):
        pass


    def test_negative_number(self):
        """
        Test case for providing a negative value for C_PTS.
        """
        input_lines = [
            'NUMPOINTS=5',
            'POINTS=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]',
            'LENGTH1=1.0',
            'RADIUS1=0.5',
            'EPSILON=1.0',
            'AREA1=10.0',
            'Q_PTS=3',
            'QUADS=2',
            'DIST=2.0',
            'N_PTS=4',
            'K_PTS=2',
            'A_PTS=1',
            'B_PTS=1',
            'C_PTS=-1',  # Inserting a negative value for C_PTS
            'D_PTS=1',
            'E_PTS=1',
            'F_PTS=1',
            'G_PTS=2',
            'LENGTH2=2.0',
            'RADIUS2=1.0',
            'AREA2=20.0',
            'LMU=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]',
            'PUV=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]'
        ]
        with self.assertRaises(Exception) as context:
            p.validate_and_parse_input(input_lines)
        self.assertEqual(str(context.exception), 'Invalid value for C_PTS')

    def test_too_small_value_NUMPOINTS(self):
        """
        Test case for providing a too small value for NUMPOINTS.
        """
        input_lines = [
            'NUMPOINTS=1', # Inserting a value for NUMPOINTS that is too small
            'POINTS=[(0, 0)]',
            'LENGTH1=1.0',
            'RADIUS1=0.5',
            'EPSILON=1.0',
            'AREA1=10.0',
            'Q_PTS=3',
            'QUADS=2',
            'DIST=2.0',
            'N_PTS=4',
            'K_PTS=2',
            'A_PTS=1',
            'B_PTS=1',
            'C_PTS=1', 
            'D_PTS=1',
            'E_PTS=1',
            'F_PTS=1',
            'G_PTS=2',
            'LENGTH2=2.0',
            'RADIUS2=1.0',
            'AREA2=20.0',
            'LMU=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]',
            'PUV=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]'
        ]
        with self.assertRaises(Exception) as context:
            p.validate_and_parse_input(input_lines)
        self.assertEqual(str(context.exception), 'Invalid value for NUMPOINTS')
    
    def test_insert_string(self):
        """
        Test case for providing a string instead of a value.
        """
        input_lines = [
            'NUMPOINTS=1', 
            'POINTS=[(0, 0)]',
            'LENGTH1=1.0',
            'RADIUS1=0.5',
            'EPSILON=1.0',
            'AREA1=10.0',
            'Q_PTS=3',
            'QUADS=2',
            'DIST=2.0',
            'N_PTS=hello_there_darkness_my_old_friend', # Inserting a string for N_PTS
            'K_PTS=2',
            'A_PTS=1',
            'B_PTS=1',
            'C_PTS=1', 
            'D_PTS=1',
            'E_PTS=1',
            'F_PTS=1',
            'G_PTS=2',
            'LENGTH2=2.0',
            'RADIUS2=1.0',
            'AREA2=20.0',
            'LMU=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]',
            'PUV=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]'
        ]
        with self.assertRaises(Exception) as context:
            p.validate_and_parse_input(input_lines)
        self.assertEqual(str(context.exception), 'Invalid value for N_PTS')
    
if __name__ == '__main__':
    unittest.main()