#Choose Your Own Adventure
#By: Taylor
print "What's your name? "
name = raw_input("My name is:  ")
name = str(name)

print "\nHello, " + name

if name == "Da Bomb":
	print "Hi, Taylor! I know it's you because Taylor is the only Da Bomb\n  "

if name == "Taylor":
	print "Wow! Nice name, You are Da Bomb! Hi, Taylor!!\n\n\n"

if name != "Taylor":
	print "You are not Da Bomb, Sorry! That Sucks for you!!! :P \n\n\n"
	

inRoom = "main"
gameOver = 0 # 0 means no, 1 means yes

if gameOver == 1:
	print "The End :D Thanks For playing! By: Taylor"

while gameOver != 1:
	if inRoom == "main":
		print name + ", you are stuck in a haunted house! Try to get out.\n"		
		print "1) Move to the rotting storage room"
		print "2) Move to the flooding bathroom"
		print "3) Move to moldy kitchen"
		print "4) The Pointless Room"
		
		action = raw_input("Choose #1-4:\n ")
		action = int(action)
		
		if action == 1:
			inRoom = "storage"
		if action == 2:
			inRoom = "bathroom"
		if action == 3:
			inRoom = "kitchen"
		if action == 4:
			inRoom = "pointless"
		if action == 5:
			inRoom = "secret"
		
	if inRoom == "storage":
		print "Eww... Can you smell that rotting pumpkin?\nEek! It's grey... and mushy... D:\n "
		print "You found a cat \(=^.^=)/"
		print "Go back!\n"
		
		print "1) Go back"
		print "2) Play with cat\n"
		
		action = raw_input("Choose #1-2:\n ")
		action = int(action)
		
		if action == 1:
			inRoom = 'main'
		if action == 2:
			print "Hahaha Fool! The cat bit you! \(=^.^=)/"
			print "pick again! "
			
			action = raw_input("There are Band-Aids in the bathroom, do you want to go there?\n\n 1) Yes, Take me to the bathroom\n 2) No, Fail the game\n\n")
			action = int(action)
		   
			if action == 1:
				inRoom = "bathroom"
			if action == 2:
				gameOver = 1
				print "Haha, Why?!?! Game Over, YOU LOSE!"
			
		
	if inRoom == "bathroom":
		print "You went into a flooded room, try to swim."
		
		print "1) Swim"
		print "2) Drown"
		print "3) Open cabinet"
		
		action = raw_input("Choose 1-3: ")
		action = int(action)
		
		if action == 1:
			print "You are smart! You lived, you can go back to main now!"
			
			action = raw_input("Go Back, it's your only choice! :P (Press 1)\n")
			action = int(action)
			 
			if action == 1:
				inRoom = 'main'
			
		if action == 2:
			print "\nYou are an idiot!\n"
			gameOver = 1
			
		if action == 3:
			print "\nAwesome! You found the Band-Aids! If you were bit by a cat...*cough* *cough* Idoit *cough*... You are ok now!\n"
			inRoom = "main"
			
		
	if inRoom == "kitchen":
		print "You found a sandwich. Yum!"
		print "Go back!\n"
		 
		print "1) Go back"
		print "2) Eat the sandwitch"
		print "3) Solve a riddle"
		
		action = raw_input("Choose #1: ")
		action = int(action)
		
		if action == 1:
			inRoom = 'main'
		if action == 2:
			print "Did you not see the mold!?!? You are now poisoned! "
			gameOver = 1
		if action == 3:
			inRoom = 'roomOfRiddles'
   
	if inRoom == "roomOfRiddles": 
			print "Welcome to the room of riddles!\n"
			print "Here you will test your smarts and duel your brain!\n"
			print "If you get the riddle correct, you may proceed. If you get the riddle wrong, you will be dropped in the pit of lava! "
			print "The best of luck to you!\n"
			
			print "Riddle 1/3: In a round house, there was a nanny, a butler, a girl, and a boy. When the mom got home, there was a stain on the floor. The mom asked who did it and here are her answers: \n" 
			
			print "1) Nanny: It wasn't me, I was vaccuming!\n"
			print "2) Butler: It wasn't me, I was searching for the kids!\n"
			print "3) Boy: I didn't do it, I was hiding in the corner from the butler!\n"
			print "4) Girl: I didn't do it, I was hiding under my bed from the butler!\n"
			
			action = raw_input (" Who did it?\n")
			action = int(action)
			
			if action == 3:
				print "Wow, you aren't so lame after all!\n\n You will be asked another riddle!"
				print "I will tell all the other games to make it harder for " + name + "!\n\n"
				
				print "Riddle 2/3: In a one story yellow house, everything is yellow. The lamp is yellow, the beds are yellow, the couch is yeller, the floor is yellow, the celing is yellow, the walls are yellow, EVERYTHING is yellow.\n"
				print "What color was the couch?\n"
				print "1) Yellow"
				print "2) Yeller"
				print "3) Black"
				print "4) There is no lamp"
				
				action = raw_input("Choose #1-4")
				action = int(action)
				
				if action == 2:
					print "I am not impressed yet, but I am judging you less.\n"
					print "I lied about the third riddle! I thought you would be in the lava pit by now. Well... this is embarassing."
					print "I guess I am required to give you the password.\n"
					
					action = raw_input ("Go back to the main room (Press 1) and go to room 5.\n No, I'm not crazy. I know there isn't a 5 option! It's a secret room!\n The password is 56! Go now! ")
					action = int(action)
					
					if action == 1:
						inRoom = 'main'	
				
				elif action != 2:
					print "You were fooled that easily? Better luck next time!\n Well, as promised, to the pit of lava you go! \n Wheeeeeew..... SPLASH!"
					gameOver = 1 
							
			elif action != 3:
					print "Wow, you failed on the first riddle? Wah wah wah wah!\n Better luck next time!"
					gameOver = 1
					
	if inRoom == "pointless":
		print "Why would you go in a pointless room?\n"
		print "The door is one way and you are stuck!\n"
		print " WOW, this will get boring quick\n"
		print "I'll just end the game here and consider you weird for going in a pointless room!\n"
		gameOver = 1
	
	
		
	if inRoom == "secret":
		print "You found a door. It's locked. It needs a passcode."
		
		action = raw_input("Do you have the code?\n If so, enter is here: ")
		action = int(action)
		
		if action == 56:
			print "\n\nYou found the exit!\n\nYou are no longer doomed!\n\nYou just won the game!\n\n"
			gameOver = 1
		
		gameOver = 1
		
	if gameOver == 1:
		print "The End :D Thanks For playing! By: Taylor Quinn"
