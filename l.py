#Guessing Game
#Author : Faith Christy
import random

guess = 0 #this is user input
secret = random,randint (0,100) ## Random number between 0 and 100

While guess = secret:
	guess = raw_input (“Please enter a number: “)
	guess = int(guess) # “1” to 1
  

 
if guess < secret: 
    print "Too Low, the flying monkeys are coming! NOOOOO!" 
elif guess > secret: 
    print "Too high, the flying monkeys are closer! RUN!"

 else:
	print “You win! The flying monkeys will not brutally murder you! Yay!"


