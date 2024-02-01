import math
import unittest
import sys
import os

# Add root folder to current path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.cmv import CMV, _determine_quadrant, _check_tripoint_radius
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
                 
    def test_determine_quadrant(self):
        self.assertIs(_determine_quadrant((0, 0)), 1)
        self.assertIs(_determine_quadrant((0, 1)), 1)
        self.assertIs(_determine_quadrant((1, 0)), 1)
        self.assertIs(_determine_quadrant((1, 1)), 1)
        self.assertIs(_determine_quadrant((1.11, 1.1414)), 1)

        self.assertIs(_determine_quadrant((-1, 0)), 2)
        self.assertIs(_determine_quadrant((-1, 1)), 2)
        self.assertIs(_determine_quadrant((-1, 1)), 2)
        self.assertIs(_determine_quadrant((-0.1, 2.4)), 2)
        
        self.assertIs(_determine_quadrant((0, -1)), 3)
        self.assertIs(_determine_quadrant((-1, -1)), 3)
        self.assertIs(_determine_quadrant((-6.3, -3.4)), 3)

        self.assertIs(_determine_quadrant((1, -1)), 4)
        self.assertIs(_determine_quadrant((0.34, -75)), 4)

    def test_check_tripoint_radius(self):
        """Tests `cmv/_check_tripoint_radius` for different types of tripoint
        setups.

        It should be able to handle randomly distributed points as well as 
        structured points, like unit vector points on the unit circle.
        """
        self.assertFalse(_check_tripoint_radius((0, 1), (1, 0), (5, 2), 1.0))
        self.assertFalse(_check_tripoint_radius((3, 4), (2, 1), (5, 2), 1.7))

        self.assertTrue(_check_tripoint_radius((0, 1), (1, 0), (-1, 0), 1.0))
        self.assertTrue(_check_tripoint_radius((3, 4), (2, 1), (5, 2), 2.0))
        self.assertTrue(_check_tripoint_radius((0, 1), (0, 0), (1, 0), 2.0))
        self.assertTrue(_check_tripoint_radius((0, 1), (0, 0), (1, 0), math.sqrt(2)))
    
    def test_condition0(self):
        filename = "cmv_cond0.in"
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        cmv.POINTS = [(0,0),(1,1)]
        cmv.NUMPOINTS = 2
        cmv.LENGTH1 = 1
        self.assertTrue(cmv.condition0())
        cmv.LENGTH1 = 2
        self.assertFalse(cmv.condition0())
        cmv.POINTS = [(-1,-1),(2,-2)]
        cmv.LENGTH1 = 1
        self.assertTrue(cmv.condition0())
        cmv.POINTS = []
        cmv.NUMPOINTS = 0
        cmv.LENGTH1 = 0
        self.assertFalse(cmv.condition0())
        cmv.POINTS = [(0,0),(0,0)]
        cmv.NUMPOINTS = 2
        self.assertFalse(cmv.condition0())

        
    def test_condition3(self):
        """
            Test the condition3 method of the CMV class.

            This method checks the behavior of the condition3 method under various scenarios:
            1. It tests if there exists at least one set of three consecutive points forming a triangle
                with an area greater than AREA1.
            2. It tests the behavior when there are not enough points (NUMPOINTS < 3), expecting the
                function to return False.
            3. It tests the behavior when the area of the triangle formed by three consecutive points
                is less than the specified AREA1, expecting the function to return False.

            Parameters:
            - self: The instance of the test class.

            Returns:
            - None
        """

        filename = "cmv_cond3.in"

        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        self.assertTrue(cmv.condition3(), "At least one set of three consecutive points forms a triangle with area greater than AREA1")

        cmv.NUMPOINTS = 2
        cmv.POINTS = [(1,2), (3,4)]
        self.assertFalse(cmv.condition3(), "Not enough points should make function return False")

        cmv.NUMPOINTS = 4
        cmv.POINTS = [(0, 0), (1, 0), (0, 1), (2, 2)]
        cmv.AREA1 = 10
        self.assertFalse(cmv.condition3(), "If the area of the triangle is less than AREA1, the function should return False")
        
    def test_condition4(self):
        # Expected data for true
        filename = "cmv_cond4_true.in"
        filepath = os.path.join(os.path.dirname(__file__), "data", filename)
        cmv = self.instantiate_object(filepath)
        self.assertTrue(cmv.condition4())

        # QUADS=3 but all points in Q1
        filename = "cmv_cond4_false.in"
        filepath = os.path.join(os.path.dirname(__file__), "data", filename)
        cmv = self.instantiate_object(filepath)
        self.assertFalse(cmv.condition4())

        # Two points cannot fulfill three quadrants
        cmv.Q_PTS = 2
        cmv.QUADS = 3
        self.assertFalse(cmv.condition4())

        # Two points cannot fulfill three quadrants
        cmv.Q_PTS = 5
        cmv.NUMPOINTS = 2
        self.assertFalse(cmv.condition4())

    def test_condition5(self):
        filename = "cmv_cond5_base.in"
        filepath = os.path.join(os.path.dirname(__file__), "data", filename)
        cmv = self.instantiate_object(filepath)

        # Two points, second has smaller X
        cmv.POINTS = [(2, 1), (1, 1)]
        cmv.NUMPOINTS = len(cmv.POINTS)
        self.assertTrue(cmv.condition5(), "Should return true when second X is smaller")

        # Two points, second has larger X
        cmv.POINTS = cmv.POINTS[::-1]
        self.assertFalse(cmv.condition5(), "Should return false when second X is larger")

        # Multiple points of equal value with one larger in the middle
        cmv.POINTS = [(1, 0), (1, 0), (2, 0), (1, 0)]
        cmv.NUMPOINTS = len(cmv.POINTS)
        self.assertTrue(cmv.condition5(), "A bigger item surrounded by smaller items should return true")

        # Multiple points of equal value with one smaller in the middle
        cmv.POINTS = [(2, 0), (2, 0), (1, 0), (2, 0)]
        cmv.NUMPOINTS = len(cmv.POINTS)
        self.assertTrue(cmv.condition5(), "A smaller item surrounded by larger items should return true")

        # All points are the same
        cmv.POINTS = [(2, 0), (2, 0), (2, 0), (2, 0)]
        cmv.NUMPOINTS = len(cmv.POINTS)
        self.assertFalse(cmv.condition5(), "A list of points with the same X should return false")

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

    def test_condition10(self):
        """
            Test the condition10 method of the CMV class.

            This method checks the behavior of the condition10 method under various scenarios:
            1. An instance where the number of points is too few
            2. An instance where the E_PTS value is invalid
            3. An instance where the F_PTS value is invalid
            4. An instance where both E_PTS and F_PTS are invalid
            5. An instance where no triangle is greater than AREA1
            6. An instance where a triangle is greater than AREA1
        """
        cmv = self.instantiate_object(os.path.join(os.path.dirname(__file__), "data", "cmv_cond10.in"))

        cmv.POINTS = [(0, 0), (1, 0), (1, 1), (0, 1), (2, 2)]
        cmv.NUMPOINTS = len(cmv.POINTS)

        # Test 1: Function should return False because there are less than 5 points
        cmv.NUMPOINTS = 4
        self.assertFalse(cmv.condition10())
        cmv.NUMPOINTS = len(cmv.POINTS)

        # Test 2: Invalid E_PTS value
        cmv.E_PTS = 0
        self.assertFalse(cmv.condition10())
        cmv.E_PTS = 1

        # Test 3: Invalid F_PTS value
        cmv.F_PTS = 0
        self.assertFalse(cmv.condition10())
        cmv.F_PTS = 1

        # # Test 4: Invalid E_PTS and F_PTS values where they are greater than NUMPOINTS
        cmv.E_PTS = 6
        cmv.F_PTS = 6
        self.assertFalse(cmv.condition10())
        cmv.E_PTS = 1
        cmv.F_PTS = 1

        # # Test 5: No Triangle is greater than AREA1
        cmv.AREA1 = 10
        self.assertFalse(cmv.condition10())
        cmv.AREA1 = 0.5

        # Test 6: Triangle is greater than AREA1
        cmv.POINTS = [(0, 0), (3, 0), (1, 2), (4, 4), (6, 6), (8, 8), (8, 8)]
        cmv.NUMPOINTS = len(cmv.POINTS)
        cmv.E_PTS = 1
        cmv.F_PTS = 1
        self.assertTrue(cmv.condition10())

    def test_condition8(self):
        """Test cases for condition 8.

        > There exists at least one set of three data points separated by
        > exactly A PTS and B PTS consecutive intervening points,
        > respectively, that cannot be contained within or on a circle of
        > radius RADIUS1. The condition is not met when NUMPOINTS < 5.
        
        Test scenarios:
        - True on [(0, 0), (1, 1), (1, 0), (1, 1), (0, 1)] R=0.5 A=B=1 (longest
          distance is sqrt(2))
        - False on [(0, 0), (1, 1), (1, 0), (1, 1), (0, 1)] R=2 A=B=1 (all
          points can be covered)
        - False on [(0, 0), (1, 1), (1, 0), (1, 1), (0, 1)] R=inf A=B=1 (all
          points can be covered)
        - True on [(0, 0), (1, 1), (1, 0), (1, 1), (0, 2)] R=0.5 A=B=1 (last
          point to far away)
        - False on NUMPOINTS < 5
        """
        
        filename = "cmv_cond8.in"
        filepath = os.path.join(os.path.dirname(__file__), "data", filename)
        cmv = self.instantiate_object(filepath)

        self.assertTrue(cmv.condition8(), "Should true; largest dist is sqrt(2) and max dist is 1")

        cmv.RADIUS1 = 2
        self.assertFalse(cmv.condition8(), "Should false; R=2 and all points are within R=sqrt(2)")

        cmv.RADIUS1 = float('inf')
        self.assertFalse(cmv.condition8(), "Should false; all distances are covered in inf radius")

        cmv.RADIUS1 = 0.5
        cmv.POINTS[4] = (0, 2)
        self.assertTrue(cmv.condition8(), "Should true; (0, 2) is too far away to be covered by R=0.5")

        cmv.POINTS = cmv.POINTS[:3]
        cmv.NUMPOINTS = len(cmv.POINTS)
        self.assertFalse(cmv.condition8(), "Should false; only contains 3 points")

    def test_condition9(self):
        """
            Test the condition9 method of the CMV class.

            This method checks the behavior of the condition9 method under various scenarios:
            1. An instance where the requirement is fulfilled
            2. Same instance with a new EPSILON s.t. the requirement no longer holds
            3. Same instance where the number of points are too few
            4. Same instance where the first point coincide with the second one, hence undefined angle
            
            Parameters:
            - self: The instance of the test class.
            
            Returns:
            - None
        """

        filename="condition9/cmv_cond9_accept.in"

        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        self.assertTrue(cmv.condition9())

        epsilon_prev = cmv.EPSILON
        cmv.EPSILON = 2.5
        self.assertFalse(cmv.condition9())

        cmv.EPSILON = epsilon_prev
        numpoints_prev = cmv.NUMPOINTS
        cmv.NUMPOINTS = 4
        self.assertFalse(cmv.condition9())

        cmv.NUMPOINTS = numpoints_prev
        points0_prev = cmv.POINTS[0]
        cmv.POINTS[0] = cmv.POINTS[2]
        self.assertFalse(cmv.condition9())

    
    def test_condition11(self):
        """
            Test cases for the condition11 cmv method.

            Test scenarios:
            1. Assert that a valid input returns True
            2. Assert that if there is no set of data points, the method returns False
            3. Assert that False is returned if the difference between X[j] and X[i] is zero
            4. Assert that the method can handle small differences, down to the 10th decimal
            5. Assert that the method can handle small differences, down to the 10th decimal
            6. Assert that False is returned if X[j] is a positive number and X[i] is a negative number
            7. Assert that True is returned when both X[i] and X[j] are negative and X[j] is less than X[i]

            Parameters:
            - self: the TestCase object

            Returns:
            None
         """
        
        #Assert that it returns True when it should
        filename = "cmv_cond11_accept.in"
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/condition11/"+filename)
        self.assertTrue(cmv.condition11())
        #Assert that it returns False when it should
        filename = "cmv_cond11_dec_obvious.in"
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/condition11/"+filename)
        self.assertFalse(cmv.condition11())
        #Test edge case when diff is zero
        filename = "cmv_cond11_dec_edge.in"
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/condition11/"+filename)
        self.assertFalse(cmv.condition11())
        #Test edge case when the 10th decimal makes it less
        filename = "cmv_cond11_acc_edge.in"
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/condition11/"+filename)
        self.assertTrue(cmv.condition11())
         #Test edge case when the 10th decimal makes it greater
        filename = "cmv_cond11_dec_10th_dec_greater.in"
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/condition11/"+filename)
        self.assertFalse(cmv.condition11())
         #Test edge case when X[i] is a negative number and X[j] is a positive number
        filename = "cmv_cond11_neg_num.in"
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/condition11/"+filename)
        self.assertFalse(cmv.condition11())
         #Test edge case when both X[i] and X[j] are negative and X[j] is less than X[i]
        filename = "cmv_cond11_both_neg.in"
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/condition11/"+filename)
        self.assertTrue(cmv.condition11())

    def test_condition12(self):
        """
            Test the condition12 method of the CMV class.

            This method checks the behavior of the condition12 method under various scenarios:
            1. An instance where the requirement is fulfilled
            2. An instance where the first requirement is fulfilled, but not the second one
            3. An instance where the second requirement is fulfilled, but not the first one
            4. An instance where the number of points does not fulfill the requirements
            
            Parameters:
            - self: The instance of the test class.
            
            Returns:
            - None
        """

        filename="condition12/cmv_cond12_accept.in"
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        self.assertTrue(cmv.condition12())

        filename="condition12/cmv_cond12_reject.in"
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        self.assertFalse(cmv.condition12())

        filename="condition12/cmv_cond12_reject2.in"
        cmv = self.instantiate_object(os.path.dirname(__file__)+"/data/"+filename)
        self.assertFalse(cmv.condition12())

        cmv.NUMPOINTS = 2
        self.assertFalse(cmv.condition12())

        
if __name__ == '__main__':
    unittest.main()
