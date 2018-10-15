''' checks the load function to ensure it loads the save file correctly. '''
''' there may be several points of failure, or the save file could be corrupt. '''
import unittest
import os.path
from load import load
 
class test_check_input(unittest.TestCase):

    def test_load(self):
    	filename = "non-existent-file.txt"
    	# test a non-existent file
    	self.assertEqual(load(filename), "No save file exists.")
    	# see if a save file exists at all

    	filename = "save.txt"
    	self.assertTrue(os.path.exists(filename))

    	for trial in range(6):
    		if trial != 0:
	    		save_file = open("save.txt", "w+")
	    		save_file.write(str(trial))
	    		save_file.close()

	    		print("test is: " + str(trial))
	    		self.assertEqual(load("save.txt"), "success")

    	bad_states = [-1, 50, 79, "egg"]
    	for trial in range(len(bad_states)):
    		save_file = open("save.txt", "w+")
    		save_file.write(str(bad_states[trial]))
    		save_file.close()

    		print("test is: " + str(bad_states[trial]))
    		self.assertEqual(load("save.txt"), "Save file is corrupted. Please start a new game.")
    	
        # self.assertEqual(check_input_verbose("7"), "\"7\" is not a valid input.")
        # self.assertEqual(check_input_verbose("2355"), "\"2355\" is not a valid input.")
        # self.assertEqual(check_input_verbose("start"), "scene1")
        # self.assertNotEqual(check_input_verbose("sstart"), "start")

