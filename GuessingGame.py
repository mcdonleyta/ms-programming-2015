score = 0 
import random
secret = random.randint(1, 100)
while True: 
    print('Pick a number between 1 and 100')
    guess = input()
    i = int(guess) 
    if i == secret: 
       print("You win")
       score = score 
       print ("Your Score: ") + str(score)
       break 
    elif i < secret: 
       print ("Too Low, try again")
       score= score + 1
    elif i > secret: 
       print ("Too high, try again")
       score= score + 1

