# Guessing Game
# by Raaghav Malik

import random

secret_number = 17
 #random.randint(1,100)
score = 0

guess = -1
	
while guess != secret_number:
	
	guess = raw_input("Guess a number from 1 to 100  ")

	guess = int(guess)
	
	if guess + 7 > secret_number and guess - 7 < secret_number:
		if guess < secret_number:
			print "Very close, but a little too low"
			score = score + 1
		else:
			print "Very close, but a little too high"
			score = score + 1
	if guess < secret_number:
		print "Guess is too low, try again!"
		score = score + 1
	elif guess > secret_number:
		print "Guess is too high, try again!"
		score = score + 1
	else:
		print "You Win!"
		print "It took you " + str(score) + " number of tries."

