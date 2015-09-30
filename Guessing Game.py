import random

secret =  random.randint(0,100) 
score = 1000
guess = -1

while (guess != secret):
    guess = raw_input("Make a guess: ") ## Lets the user type input
    guess = int(guess) ## Make sure input is a number

    if guess == secret:
        score = score + 10
        print "You Win"
        print "Your Score: " + str(score)
        print "Thanks for playing! :D"
        print "This game was made by Taylor"
    if guess != secret:
        score = score - 10
        if guess < secret:
            print "Too Low, try again!"
        if guess > secret:
            print "Too High, try again!"
            
