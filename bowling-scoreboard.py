#!/url/bin/python

# Filename: bowling-scoreboard.py 
# To run this code: python bowling-scoreboard 8 1 10 5 5 8 0 10 10 9 1 8 1 9 1 10 7 2

def scoreBowling(input):
	pass

def scoreCalcutator(throw, throw1, throw2):
	pass

def scoreBoardTable(throw1, throw2, last, total):
	pass

import sys 

cases = {
    'X' : 10,
    '/' : 10,
    '-' : 0,
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10': 10}

# Read all the arguments after bowling-scoreboard
for arg in sys.argv[1:]: 
	try:
		# Open the file with scores
		f = open('./tests/' + str(arg), 'r')
		content = f.readline()
		# Close file 
		f.close()

		inputValues = content.split()
		print inputValues
		
		# Send the input to score Bowling
		for s in range(0, len(inputValues)):
			print type(cases[inputValues[s]])
	except IOError:
		# If can't open the file
		print 'Cannot open', arg
		print 'Please move', arg, 'to the tests folder.'

