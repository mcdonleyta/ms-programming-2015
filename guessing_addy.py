import random

#Guessing Game
#Author: Addy
guess = 0 #This is user input
secret = random.randint(0, 100) ##Random number between 0 and 100


while guess!=secret:
	guess = raw_input("Please enter a number:")
	guess = int(guess) # "1" to 1

	if guess < secret:
		print "Guess is too low, try again!"
	elif guess > secret:
		print "Guess is too high, try again!"
	else:
		print "You Win"
	






