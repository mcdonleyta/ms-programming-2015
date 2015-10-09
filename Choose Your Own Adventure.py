

print (" what your name:")
name = raw_input("What is your name?\n")
name = str(name)
inRoom = "main"
gameOver = 0 # 0 = false, 1 = true

print "\nHello, " + name

if name == "Ansley": 
	print " You're are the BEST!! :D"
if name != "Ansley": 
	print " You're are not the best :(  So you suck"
	
	if gameOver == 1:
		print " thaks for playing! this game is made by Ansley!"
while gameOver != 1:
	if inRoom == "main":
		print " You are in an abandoned town"

		print "1)  Go into the cafe. "
		print "2)  Go check out a hole."
		print "3)  Talk to the person in front of you."
		print "4)  Run away!!"

		
		action = raw_input("Choose 1-4")
		action = int(action)
		
		
		if action == 1:
				print " You found a salad"
				print "1) eat the salad"
				print "2) drink the water behind the salad"
				print "3) move on and don't touch either"
			
				action = raw_input("Choose 1-4")
				action = int(action)
					
				if action == 1:
					print " you DIED!!!!!"
					print " Thanks for playing. This game is made by Ansley Herron :)"
					gameOver = 1
				
				if action == 2:
					print " You drank poison!!!! You died!"
					print " Thanks for playing. This game is made by Ansley Herron :)"
					gameOver = 1
						
				if action == 3:
						print " You lived!"
				print "1) go up the stairs"
				print "2) grab the keys"
				print "3) open the door"
			
				action = raw_input("Choose 1-3")
				action = int(action)
			
				if action == 1:
					print " You were walking up the staires and as you see the upstairs the staires colaspe and you fall and die!"
					print " Thanks for playing. This game is made by Ansley Herron :)"
					gameOver = 1
				
				if action == 2:
					print " You grab the keys and run for the car outside"
					
				if action == 3:
					print " You opened the door and you found one millin dollars!!!!"
				
		
				if action == 3:
					print " WOW YOU ARE GREADY aren't you!"
					gameOver = 1 
						
						
				if action == 2: 
					print "1) you get in the car and its out of gas!"
					print "2) you go grab the gas." 
				
					action = raw_input("Choose 1-2")
					action = int(action)
				
				if action == 1: 
					print " You run out of the car to grab the gas but you fall in the hole and die!"
					gameOver = 1
					
				if action == 2:
					print " You run to the car!"
					
				if action == 2:
					print "1) turn on the car!"
					print "2) Blow up the town!"
					 
					action1 = raw_input("Choose 1-2")
					action1 = int(action)
					
					if action1 == 1:
						print " YOU WON AND DID NOT DIE!!!"
						print " Thanks for playing this game is made by Ansley Herron"
						gameOver = 1
						 
					if action1 == 2: 
					   print " Your an idiot you blew your self up"
					   gameOver = 1
						
						
					if action1 == 2:
						print " You are stuiped! who goes and check out a hole!"
						gameOver = 1
			
		if action == 3: 
			print " cough* Why would you talk to a person in an abounden twon cough*"
			print "1) listen to the person"
			print "2) run away"
			action = raw_input("Choose 1-2")
			action = int(action)
					
			if action == 1:
				print " The peron tells you to go to the hole"
			
			if action == 2:
				print " you ran to far and a lion ate you"
				gameOver = 1
				
	if action == 1:
			print "1) move to the left"
			print "2) the person comes up behind you and...."
			
			action = raw_input("Choose 1-2")
			action = int(action)
				
			if action == 1:
				print " WOW you are smart! The person fell in the hole"
				print " YOU WON!!!!!!!"
				gameOver = 1
			
			if action == 2:
				print " theperson pushed you and you died"
				gameOver = 1			
			
			if action == 4:
			   print " WOW you ran and forgot WATER"
			   gameOver = 1
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
					
				
		
	
						
						
								
					
			
			
			
			
		



























