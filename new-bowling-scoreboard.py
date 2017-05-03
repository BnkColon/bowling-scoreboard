#!/url/bin/python

# Filename: new-bowling-scoreboard.py 
# To run this code: python new-bowling-scoreboard.py 8 1 10 5 5 8 0 10 10 9 1 8 1 9 1 10 7 2	

# Instructions to run the scoreboard
def instructions():
	message = (
		"""--------------------------------------------------------------------------\n"""
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

# A bowling game have ten frames
def frame():
	# Create empty dictionary
	frames = dict()

	# Add the frame keys
	frames = frames.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	
	for frameNum in range(1,11):
		frames[frameNum]=[None, None, None, None]
	#return a dictionary with 10 frames for the game
	return frames

# Frame Content
def frameContent(frameT, frameNumber, content):
	if frameNumber in range(1,11):
#		frameT[frameNumber] = content
		if content == 10:
			strike()
		elif content == 0:
			pass

	else:
		print "ERROR"
	return frameT

# Roll 1 of the frame.
def roll1(frameT, frameNumber, pinsNumber1):
 	if pinsNumber == 10:
 		frameContent(frame, frameNumber, pinsNumber1)
 		return strike()
 	else:
 		roll2(pinsNumber1)

# Roll 2 of the frame.
def roll2(frameT, frameNumber, pinsNumber2):
 	pass

# Roll 3 is a special case for frame 10.
def roll3(frameT, frameNumber, pinsNumber3):
 	pass


# STRIKE - 10 pins knocket in the Roll 1
def strike():
	# ASCII Text Signature Generator / Figlet Frontend 
	# (Font: 'varsity')
	# http://www.kammerl.de/ascii/AsciiSignature.php
	print  """  ______   _________  _______     _____  ___  ____   ________ """
	print  """.' ____ \ |  _   _  ||_   __ \   |_   _||_  ||_  _| |_   __  |"""
	print  """| (___ \_||_/ | | \_|  | |__) |    | |    | |_/ /     | |_ \_|"""
	print  """ _.____`.     | |      |  __ /     | |    |  __'.     |  _| _ """
	print  """| \____) |   _| |_    _| |  \ \_  _| |_  _| |  \ \_  _| |__/ |"""
	print  """ \______.'  |_____|  |____| |___||_____||____||____||________|"""

# SPARE - 10 pins knocket in Roll 1 + Roll 2
def spare():
	# ASCII Text Signature Generator / Figlet Frontend 
	# (Font: 'varsity')
	# http://www.kammerl.de/ascii/AsciiSignature.php
	print  """  ______   _______     _       _______     ________ """
	print  """.' ____ \ |_   __ \   / \     |_   __ \   |_   __  |"""
	print  """| (___ \_|  | |__) | / _ \      | |__) |    | |_ \_|"""
	print  """ _.____`.   |  ___/ / ___ \     |  __ /     |  _| _ """
	print  """| \____) | _| |_  _/ /   \ \_  _| |  \ \_  _| |__/ |"""
	print  """ \______.'|_____||____| |____||____| |___||________|"""

# MISS - 0 pins knocket
def miss():
	# ASCII Text Signature Generator / Figlet Frontend 
	# (Font: 'varsity')
	# http://www.kammerl.de/ascii/AsciiSignature.php
	print """ ____    ____  _____   ______    ______  """
	print """|_   \  /   _||_   _|.' ____ \ .' ____ \ """
	print """  |   \/   |    | |  | (___ \_|| (___ \_|"""
	print """  | |\  /| |    | |   _.____`.  _.____`. """
	print """ _| |_\/_| |_  _| |_ | \____) || \____) |"""
	print """|_____||_____||_____| \______.' \______.'"""

# Total of Roll 1 + Roll 2 + Roll 3 
def total(pinsNumber1, pinsNumber2, pinsNumber3):
 	total = pinsNumber1 + pinsNumber2 + pinsNumber3
 	return total

# Insert Roll 1, Roll 2, Roll 3 and total
def scoreboard():
 	pass

# inputValues - Read all the arguments after bowling-scoreboard.py <numbers>
def game(inputValues=sys.argv[1:]):

	# 10 clean frames
	frames = frame()
	print frames
	# for frameNumber in range(1,11): 
	# # for each number received in sys
	# 	for number in range(len(inputValues)):
	# 		# Call stringToInt function to change the values received from sys
	# 		frameContent(frames, frameNumber, stringToInt(inputValues[number]))
			
if __name__ == '__main__':
    game()