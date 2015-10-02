#FF0000#36FF00#36FF00#Guessing Game
#Author: Kavin Maryala
import random


guess = -1
secret = random.randint (0, 100)
score = 0 
print "How score works: When you guess you get 1 point the more points the worse it gets. Aim for less points, and have some fun :)"
while guess != secret:
	guess = raw_input("Please enter a number: ")
	guess = int(guess)
	score = score + 1

	if guess < secret:
		print "Guess is too low, you got Demaciad by Garen die. :("
	elif guess > secret:
		print "Guess is too high, you got Dunked by Darius die. :("
	else:
		print "You didn't get one shot by Veigar so you win. "
		print "Your score is " + str(score)
