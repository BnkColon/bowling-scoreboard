#!/url/bin/python

# Filename: bowling-scoreboard.py 
# To run this code: python bowling-scoreboard 8 1 10 5 5 8 0 10 10 9 1 8 1 9 1 10 7 2

def scoreBoardCalcutator(number):
	# Frames
	scoreBoard = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None}

	## Strike
	if number == 10:
		print 'Strike'

	## Spare
	#if number + (number+1) == 10:
	#	print 'Spare'

	## Miss 
	if number == 0:
		print 'Miss'

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

