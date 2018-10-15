import unittest
from check_input import check_input_verbose
 
class test_check_input(unittest.TestCase):

    def test_input(self):
        self.assertEqual(check_input_verbose("egg"), "\"egg\" is not a valid input.")
        self.assertEqual(check_input_verbose("7"), "\"7\" is not a valid input.")
        self.assertEqual(check_input_verbose("2355"), "\"2355\" is not a valid input.")
        self.assertEqual(check_input_verbose("start"), "scene1")
        self.assertNotEqual(check_input_verbose("sstart"), "start")

