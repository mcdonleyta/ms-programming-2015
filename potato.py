import random
score = 0
guess = 12 
secret = random.randint(0, 100)
while guess != secret:
	
	guess = raw_input("type a number: ")
	guess = int(guess)
	score = score + 1
	if guess < secret:
		print "Guess is to low, try another number."
	elif guess > secret:
		print "Guess is to high, try another number."
	else:
		print "You've won!", score
