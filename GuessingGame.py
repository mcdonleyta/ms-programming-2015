


import random 

print ( "Hello User") 

# Guessing Game 
# Athour Nivaas

guess = -1 # -1 means user has not guessed 
secert = random.randint (0,100) ## Random number between 0 and 100 

while guess != secert:## Repeat until they win
	guess = raw_input  ("please put in number: ") 
	guess = int(guess) # "1"  to 1

	if guess > secert:
		print "Guess is to high try again"
	elif guess < secert: 
		print "guess is to low" 
		print "try again"  
	elif  guess == secert:
		 print "you win"
