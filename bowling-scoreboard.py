#!/url/bin/python

# Filename: bowling-scoreboard.py 
# To run this code: python bowling-scoreboard 8 1 10 5 5 8 0 10 10 9 1 8 1 9 1 10 7 2

def scoreCalcutator(throw, throw1, throw2):
	if int(throw) == 10:
		total = 10 + throw1 + throw2
	else:
		if throw + throw1 == 10:
			total = 10 + throw2
		else:
			total = throw + throw1
	return total 

def scoreBoardTable(throw1, throw2, last, total):
	scoreBoard = {1: (None, None, None, None), 2: (None, None, None, None), 3: {None, None, None, None}, 4: {None, None, None, None}, 5: {None, None, None, None}, 6: {None, None, None, None}, 7: {None, None, None, None}, 8: {None, None, None, None}, 9: {None, None, None, None}, 10: {None, None, None, None}}
	total += int(total)
	for frame,score in scoreBoard.items():
		if scoreBoard[frame][0] == None:
			scoreBoard[frame] = {throw1, throw2, last, total}
		else: 
			continue
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
		for s in range(0, len(score),2):
			if score[s] == '10':
				total = scoreCalcutator(int(score[s]), int(score[s+1]), int(score[s+2]))
				final = scoreBoardTable('X', 0, 0, int(total))
			elif score[s] == '0':
				if score[s+1] != '10':
					total = scoreCalcutator(int(score[s]), int(score[s+1]), 0)
					final = scoreBoardTable(int(score[s]), int(score[s+1]), 0, int(total))
				else:
					total = scoreCalcutator(int(score[s]), int(score[s+1]), int(score[s+2]))
					final = scoreBoardTable(int(score[s]), int(score[s+1]), 0, int(total))
			else:
				total = scoreCalcutator(int(score[s]), int(score[s+1]), 0)
				final = scoreBoardTable(int(score[s]), int(score[s+1]), 0, int(total))
		print final
	except IOError:
		# If can't open the file
		print 'Cannot open', arg
		print 'Please move', arg, 'to the tests folder.'

