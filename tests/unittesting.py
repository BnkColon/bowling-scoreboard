#!/url/bin/python

# File name: unittesting.py

# This is the unit test file for the bowling score calculation problem

# https://docs.python.org/2/library/unittest.html
import unittest

class testBowlingScore(unittest.TestCase):
	"""docstring for testBowlingScore"""

	def runTest(self, arg):
		super(testBowlingScore, self).__init__()
		self.arg = arg

		
if __name__ == '__main__':
    unittest.main()