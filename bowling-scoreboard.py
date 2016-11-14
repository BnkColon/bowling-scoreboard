#!/url/bin/python

# Filename: bowling-scoreboard.py 
# To run this code: python bowling-scoreboard 8 1 10 5 5 8 0 10 10 9 1 8 1 9 1 10 7 2

def scoreBoardCalcutator(number):
	# Frames
	scoreBoard = dict()

	## Strike

	## Spare

	## Miss 
	return scoreBoard


import sys 

# Read all the arguments after bowling-scoreboard
for arg in sys.argv[1:]: 
	try:
		# Open the file with scores
		f = open('./tests/' + str(arg), 'r')
		score = f.readline()
		# Close file 
		f.close()

		score = score.split()
		
		# Send all the scores to the Board Calculator
		for s in score:
			scoreBoardCalcutator(s)

	except IOError:
		# If can't open the file
		print 'Cannot open', arg
		print 'Please move', arg, 'to the tests folder.'

