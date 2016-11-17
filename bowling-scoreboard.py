#!/url/bin/python

# Filename: bowling-scoreboard.py 
# To run this code: python bowling-scoreboard 8 1 10 5 5 8 0 10 10 9 1 8 1 9 1 10 7 2

def scoreBowling(input):
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

		# Split by space and save content in list.
		inputValues = content.split() 
		
		# Let the game start!!
		frameID = 1 			# Frame counter
		finalScoreFrame = 0		# Final Score
		
		# Create empty dictionary
		tableContent = dict() 			

		# Add the frame keys
		tableContent = tableContent.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
		

		for s in range(0, len(inputValues)):
			if frameID <= 10 and finalScoreFrame <= 300: # We are under the limits of the game.
				
				if cases[inputValues[s]] == 10: 	# We have a strike!
					finalScoreFrame += cases[inputValues[s]] + cases[inputValues[s+1]] + cases[inputValues[s+2]] 
					tableContent[frameID]=(cases[inputValues[s]], None, None, finalScoreFrame)
					frameID += 1
					
				elif cases[inputValues[s]] == 0:	# We have a miss!
					if tableContent[frameID] == None: # This means that this is the first throw of this frame
						tableContent[frameID]=(cases[inputValues[s]], None, None, finalScoreFrame)
						
					else:
						finalScoreFrame += cases[inputValues[s-1]] + cases[inputValues[s]] 
						tableContent[frameID]=(cases[inputValues[s-1]], cases[inputValues[s]], None, finalScoreFrame)
						frameID += 1

				else:
					if tableContent[frameID] == None: # This means that this is the first throw of this frame
						tableContent[frameID]=(cases[inputValues[s]], None, None, finalScoreFrame)
					
					else:
						if cases[inputValues[s-1]] + cases[inputValues[s]] == 10: # We have a spare!
							finalScoreFrame += cases[inputValues[s-1]] + cases[inputValues[s]] + cases[inputValues[s+1]] 
							tableContent[frameID]=(cases[inputValues[s-1]], cases[inputValues[s]], None, finalScoreFrame)
							frameID += 1
						else:
							finalScoreFrame += cases[inputValues[s-1]] + cases[inputValues[s]] 
							tableContent[frameID]=(cases[inputValues[s-1]], cases[inputValues[s]], None, finalScoreFrame)
							frameID += 1
		print tableContent



	except IOError:
		# If can't open the file
		print 'Cannot open', arg
		print 'Please move', arg, 'to the tests folder.'

