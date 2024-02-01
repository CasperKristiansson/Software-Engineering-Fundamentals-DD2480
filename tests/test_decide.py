import unittest
import sys
import os


# Add root folder to current path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


import src.decide as d

class Test_DECIDE(unittest.TestCase):

    def test_decide_all_puv_0(self):
        """
            This test confirms that the whole DECIDE pipeline works by using a test case where
            all elements in PUV are 0. This will automatically set LAUNCH to "YES"
        """

        filename='decide_accept.in'
        LAUNCH = d.instantiate_input(os.path.dirname(__file__)+"/data/decide/"+filename)
        self.assertTrue(LAUNCH)

    def test_decide_not_all_puv_0(self):
        """
            This test confirms that the whole DECIDE pipeline works by using a test case where
            not all elements in neither PUV nor PUM are 0. This will automatically set LAUNCH to "NO"
        """

        filename='decide_decline.in'
        LAUNCH = d.instantiate_input(os.path.dirname(__file__)+"/data/decide/"+filename)
        self.assertFalse(LAUNCH)

    def test_decide_all_pum_1(self):
        """
        This test confirms that the launch goes through just depending on the PUM matrix without depending on PUV
        """
        filename='decide_accept_without_puv.in'
        LAUNCH = d.instantiate_input(os.path.dirname(__file__)+"/data/decide/"+filename)
        self.assertTrue(LAUNCH)