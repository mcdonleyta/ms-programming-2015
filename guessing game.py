# this is a guessing game
# author is max

import random

secret = random.randint(0,100)
guess = -1

score = 0

print "You will try to guess the number then and every time you guess your score gets higher.  The lower the score and amount of guesses, the better."

while guess != secret:
	guess = raw_input("what is your guess?")
	
	guess = int(guess)
	
	score = score + 1
	
	if guess < secret:
		print "too low try again"
	if guess > secret:
		print "too high try again"

	elif guess == secret:
		print "you are correct, you win and your score is", score












