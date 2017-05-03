#!/url/bin/python

# Filename: new-bowling-scoreboard.py 
# To run this code: python new-bowling-scoreboard.py 8 1 10 5 5 8 0 10 10 9 1 8 1 9 1 10 7 2	

# Instructions to run the scoreboard
def instructions():
	message = ("""--------------------------------------------------------------------------\n"""
				"""To execude this code you have to write:\n"""
				"""$ python bowling-scoreboard.py <numbers>\n"""
				"""<numbers> = Numbers from 0 - 10, separated by spaces\n"""
				"""Example: python new-bowling-scoreboard.py 8 1 10 5 5 8 0 10 10 9 1 8 1 9 1 10 7 2\n"""
				"""--------------------------------------------------------------------------""")
	return message

import sys 

# Change the string to int
def stringToInt(string):
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
	return cases[string]

# Read all the arguments after bowling-scoreboard.py <numbers>
def game(inputValues=sys.argv[1:]):

	# Create empty dictionary
	frames = dict()

	# Add the frame keys
	frame = frames.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

	for number in range(len(inputValues)):
		# Call stringToInt function to change the values received from sys
		for frameNumber in range(1,11): 
			frame[frameNumber]=stringToInt(inputValues[number])

# Roll 1 of the frame.
def roll1():
 	pass

# Roll 2 of the frame.
def roll2():
 	pass

# Roll 3 is a special case for frame 10.
def roll3():
 	pass

# A bowling game have ten frames
def frameContent():
	dic
	return frames

# STRIKE - 10 pins knocket in the Roll 1
def strike():
	pass

# SPARE - 10 pins knocket in Roll 1 + Roll 2
def spare():
	pass

# MISS - 0 pins knocket
def miss():
	pass

# Total of Roll 1 + Roll 2 + Roll 3 
def total():
 	pass 

# Insert Roll 1, Roll 2, Roll 3 and total
def scoreboard():
 	pass

if __name__ == '__main__':
    game()