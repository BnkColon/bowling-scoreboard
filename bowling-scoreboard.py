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
			# We are under the limits of the game.
			if frameID <= 10 and finalScoreFrame <= 300:

				# We are in frame 10 and we have a strike!
				if frameID == 10 and cases[inputValues[s]] == 10:	
					print '1010'
					finalScoreFrame += cases[inputValues[s]] + cases[inputValues[s+1]] + cases[inputValues[s+2]] 
					tableContent[frameID]=('X', cases[inputValues[s+1]], cases[inputValues[s+2]], finalScoreFrame)
					frameID += 1
				
				# We have a strike!
				elif cases[inputValues[s]] == 10: 	
					finalScoreFrame += cases[inputValues[s]] + cases[inputValues[s+1]] + cases[inputValues[s+2]] 
					tableContent[frameID]=('X', None, None, finalScoreFrame)
					frameID += 1
					
				# We have a miss!	
				elif cases[inputValues[s]] == 0:
					# This means that this is the first throw of this frame	
					if tableContent[frameID] == None: 
						tableContent[frameID]=(cases[inputValues[s]], None, None, finalScoreFrame)
						
					else:
						finalScoreFrame += cases[inputValues[s-1]] + cases[inputValues[s]] 
						tableContent[frameID]=(cases[inputValues[s-1]], cases[inputValues[s]], None, finalScoreFrame)
						frameID += 1

				else:
					# This means that this is the first throw of this frame
					if tableContent[frameID] == None: 
						tableContent[frameID]=(cases[inputValues[s]], None, None, finalScoreFrame)
					
					else:
						# We have a spare!
						if cases[inputValues[s-1]] + cases[inputValues[s]] == 10: 
							finalScoreFrame += cases[inputValues[s-1]] + cases[inputValues[s]] + cases[inputValues[s+1]] 
							tableContent[frameID]=(cases[inputValues[s-1]], '/', None, finalScoreFrame)
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

