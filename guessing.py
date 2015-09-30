print "Hello Player, ARE YOU READY?"

import random


guess = -1
secret =  random.randint(1,100)
score = 1

while guess != secret:
	guess = raw_input("Please enter a number: ")
	guess = int(guess)

	if guess == secret:
		print "You win!"
		print "Your Score: "+ str(score)
	if guess != secret:
		score = score + 1
		if guess < secret:
			print "Too Low, Try again"
		if guess > secret:
			print "too high, try again"
