#!/usr/bin/python

# File name: unittesting.py

# This is the unit test file for the bowling score calculation problem

# https://docs.python.org/2/library/unittest.html
import unittest
from bowling_scoreboard import bowlingGame,printTable

class testBowlingScore(unittest.TestCase):
	"""docstring for testBowlingScore"""
	def __init__(self, testName, inputValues):
		super(testBowlingScore, self).__init__(testName)  # calling the super class init varies for different python versions.  This works for 2.7
		self.values = inputValues

	def setUp(self):
		self.table = bowlingGame(self.values)

	def tearDown(self):
		self.table = None

	def test_valid_table(self):
		self.assertIsNotNone(self.table, 'Table is not valid, table is None')

	def test_score_lore_300(self):
		self.assertLess(self.table[10][3], 301)

	def test_empty_table(self):
		pass

def suite(inputValues):
	suite = unittest.TestSuite()
	suite.addTest(testBowlingScore('test_valid_table',inputValues))
	if len(inputValues) > 20:
		suite.addTest(testBowlingScore('test_score_lore_300',inputValues))
	#elif len(inputValues) == None:



	return suite		
if __name__ == '__main__':
	bowlingGameTestSuite1 = suite(["8","1","10","5","5","8","0","10","10","9","1","8","1","9","1","10","7","2"])
	bowlingGameTestSuite2 = suite(["3","5","10","5","5","8","0","10","10","9","1","8","1","9","1","10","7","2"])
	bowlingGameTestSuite3 = suite(["3","5","10","5","5","8","0","10"])
	bowlingGameTestSuite4 = suite(["3"])
	bowlingGameTestSuite5 = suite([])
	bowlingGameTestSuite6 = suite(["10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10"])
	bowlingGameTestSuite7 = suite(["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"])
	bowlingGameTestSuite8 = suite(["5", "5", "5", "5", "5", "5", "5", "5", "5", "5", "5", "5", "5", "5", "5", "5", "5", "5", "5", "5", "5", "5", "5"])
	unittest.TextTestRunner(verbosity=2).run(bowlingGameTestSuite1)
	unittest.TextTestRunner(verbosity=2).run(bowlingGameTestSuite2)
	unittest.TextTestRunner(verbosity=2).run(bowlingGameTestSuite3)
	unittest.TextTestRunner(verbosity=2).run(bowlingGameTestSuite4)
	unittest.TextTestRunner(verbosity=2).run(bowlingGameTestSuite5)
	unittest.TextTestRunner(verbosity=2).run(bowlingGameTestSuite6)
	unittest.TextTestRunner(verbosity=2).run(bowlingGameTestSuite7)
	unittest.TextTestRunner(verbosity=2).run(bowlingGameTestSuite8)