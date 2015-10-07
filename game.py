import random
guess = -45
secret = random.randint(0,1000)
score = 1

while guess !=secret:
	guess =  raw_input("Please enter a number: ")
	guess = int(guess)
	
	if guess == secret: 
		print "You win, the airplane landed proply and no one was injured."
		print "Your Score: " + str(score) 
	if guess != secret: 
		score = score + 1 
	if guess < secret: 
		print "Too Low, the airplane is going to hit the new b 797-900"
	else
		print "Too high, The airplane is going to hit the sr-71 spyplane"
