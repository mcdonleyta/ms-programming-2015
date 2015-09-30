import random


guess = -1
secret = random.randint(1, 100)
score = 0 
print "Pick a number between 1 and 100"
while guess != secret:
	guess = raw_input("Please enter a number: ")
	guess = int(guess)
	score = score + 1

	if guess < secret:
		print "Too low, try again"
	elif guess > secret:
		print "Too high, try again"
	else:
		print "You win"
		print "Your score is " + str(score)
