#!/usr/bin/python

# Filename: bowling_scoreboard.py
# To run this code: python bowling_scoreboard 8 1 10 5 5 8 0 10 10 9 1 8 1 9 1 10 7 2

def instructions():
	message = ("""--------------------------------------------------------------------------\n"""
				"""To execude this code you have to write:\n"""
				"""$ python bowling-scoreboard.py <numbers>\n"""
				"""<numbers> = Numbers from 0 - 10, separated by spaces\n"""
				"""Example: python bowling-scoreboard 8 1 10 5 5 8 0 10 10 9 1 8 1 9 1 10 7 2\n"""
				"""--------------------------------------------------------------------------""")
	return message

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

def bowlingGame(inputValues=sys.argv[1:]):
	# Read all the arguments after bowling-scoreboard.py <numbers>
	try:

		# Let the game start!!
		frameID = 1 			# Frame counter
		finalScoreFrame = 0		# Final Score

		# Create empty dictionary
		tableContent = dict()

		# Add the frame keys
		tableContent = tableContent.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

		# Then we have a game
		if len(inputValues) > 0:
			try:
				for s in range(0, len(inputValues)):
					# We are under the limits of the game.
					if frameID <= 10 and finalScoreFrame <= 300:

						# We are in frame 10 and we have a strike!
						if frameID == 10 and cases[inputValues[s]] == 10:
							finalScoreFrame += cases[inputValues[s]] + cases[inputValues[s+1]] + cases[inputValues[s+2]]
							tableContent[frameID]=('X', cases[inputValues[s+1]], cases[inputValues[s+2]], finalScoreFrame)
							frameID += 1

						# We have a strike!
						elif cases[inputValues[s]] == 10:
							tableContent[frameID]=('X', ' ', ' ', finalScoreFrame)
							finalScoreFrame += cases[inputValues[s]] + cases[inputValues[s+1]] + cases[inputValues[s+2]]
							tableContent[frameID]=('X', ' ', ' ', finalScoreFrame)
							frameID += 1

						# We have a miss!
						elif cases[inputValues[s]] == 0:

							# This means that this is the first throw of this frame
							if tableContent[frameID] == None:
								tableContent[frameID]=(cases[inputValues[s]], ' ', ' ', finalScoreFrame)

							else:
								finalScoreFrame += cases[inputValues[s-1]] + cases[inputValues[s]]
								tableContent[frameID]=(cases[inputValues[s-1]], cases[inputValues[s]], ' ', finalScoreFrame)
								frameID += 1

						else:
							# This means that this is the first throw of this frame
							if tableContent[frameID] == None:
								tableContent[frameID]=(cases[inputValues[s]], ' ', ' ', finalScoreFrame)

							else:
								# We have a spare!
								if cases[inputValues[s-1]] + cases[inputValues[s]] == 10:
									finalScoreFrame += cases[inputValues[s-1]] + cases[inputValues[s]] + cases[inputValues[s+1]]
									tableContent[frameID]=(cases[inputValues[s-1]], '/', ' ', finalScoreFrame)
									frameID += 1
								elif cases[inputValues[s-1]] + cases[inputValues[s]] > 10:
									print "Error: Looks like we have an extra pin in the roll, sorry!"
									print "Please throw the ball again."
								else:
									finalScoreFrame += cases[inputValues[s-1]] + cases[inputValues[s]]
									tableContent[frameID]=(cases[inputValues[s-1]], cases[inputValues[s]], ' ', finalScoreFrame)
									frameID += 1

				return tableContent

			except IndexError:
				# If he can't calculate the Bonus values means the game is not finished.
				print ''
				print "The game is not over yet. Have Fun!"
				return tableContent
		else:
			print instructions()

	except KeyError:
		print instructions()

	return None

def printTable(tableContent):
	try:

		if tableContent[1] != None:
			# Bold the letters
			start = "\033[1m"
			end = "\033[0;0m"

			# Print the table
			print ""
			print start+"Bowling Game"+end
			print "-------------------------------------------"
			print "{:<8} {:<8} {:<8} {:<8} {:<8}".format('FR','R1', 'R2', 'R3', 'Score')
			print "-------------------------------------------"
			for k,v in tableContent.iteritems():
				r1, r2, r3, total = v
				print "{:<8} {:<8} {:<8} {:<8} {:<8}".format(k,r1, r2, r3, total)
				print "-------------------------------------------"
			print ""
		#else:
		#	print "Good game!"

	except TypeError:
		# "Can't" handle the 'X', '/' symbols."
		pass

if __name__ == '__main__':
    printTable(bowlingGame())
