#Guessing Game
#By: Ansley

score = 100
print " Welcome to the Guessing Game"
import random


guess = 0


 # this is user imput
secret = random.randint(0,100)


while guess != secret:
	guess = raw_input(" please enter a number: ")
	guess = int(guess)

	if guess < secret:
		print "guess is too low try again"
		score = score - 10
	if guess > secret:
		print "guess is too high, try again"
		score = score - 10
	if guess == secret:
		print " you win"
		score = score + 10
		print int(score)
