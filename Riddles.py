#Riddles.py

import csv
import io
import os.path

GLOBAL_PATH = ""

class Riddle:

	def __init__(row):
		#Row number of the CSV for the riddle or anagram or whatever, my current idea is a two column CSV with the left column being the riddle and the right column being the solution
		riddlefile = open(GLOBAL_PATH + "\riddles.csv")
		reader = csv.reader(riddlefile)
		for x in range(row):
			next(riddlefile)
		row = next(riddlefile)
		self.riddle = row[0]
		self.solution = row[1]
		
	def solutionCheck(attempt):
		if attempt == self.solution:
			return True
		return False
		
	def getRiddle():
		return self.riddle