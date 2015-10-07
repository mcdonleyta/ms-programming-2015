# comment
# R: Rchel Qu
import random 

guess  = 1 #This is user input
secret = random.randint(0,100) ## Random number

while guess != secret:
	guess = raw_input("please enter a number")
	guess = int(guess)
    
    
	if guess < secret:
		print "too low, Try again!"
	elif  guess > secret:
		print "too high,Try again!"
	else:
		print "You win"	
		
		
		



