#!/url/bin/python

# Filename: bowling-scoreboard.py 
# To run this code: python bowling-scoreboard 8 1 10 5 5 8 0 10 10 9 1 8 1 9 1 10 7 2

def scoreCalcutator(number, bonus1, bonus2):
	pass

def scoreBoard(number):
	scoreBoard = {1: {None, None, None, None}, 2: {None, None, None, None}, 3: {None, None, None, None}, 4: {None, None, None, None}, 5: {None, None, None, None}, 6: {None, None, None, None}, 7: {None, None, None, None}, 8: {None, None, None, None}, 9: {None, None, None, None}, 10: {None, None, None, None}}
	for k,v in scoreBoard.items():
		scoreBoard[k] = int(number)
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
		print score
		
		# Send all the scores to the Board Calculator
		for s in range(0, len(score)):
			
			if score[s] == '10':
				total = scoreCalcutator(score[s], score[s+1], score[s+2])
				scoreBoard('X', 0, 0, total)

			elif score[s] == '0':
				print 'Miss', score[s]
			else:
				print 'Score', score[s]
		
	except IOError:
		# If can't open the file
		print 'Cannot open', arg
		print 'Please move', arg, 'to the tests folder.'

