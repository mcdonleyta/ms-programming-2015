inRoom = "main"
hasKey = 0 
hasEscaped = 0 
 
while hasEscaped == 0: 
	if inRoom == "west":
		print
		print "You come across a room with two doors and two twins."
		print "There is sign that says: "
		
		print
		print "One twin always lies."
		print "The other one always says the truth."
		print "One of these doors is the right way."
		print "The other one is a trap."
		print "You are allowed only one question to one of these twins."
		print 
		
		answer1 = raw_input("What question should you ask?   ")
		
		if answer1 == "If I asked the other twin which door is the right way what would he say?":
			print
			print '''The twin you asked answered,"The other twin would say that the left door is the correct one.'''
			
			print
			print "1) left door"
			print "2) right door"
			print
			
			whichDoor = raw_input("Which door should you enter?   ")
			whichDoor = int(whichDoor)
			
			if whichDoor == 1:
				print
				print "You enter a long corridor."
				print "You keep running to the end, but there is no end"
				print "You try running back, but you never get back to the door you used to enter"
				print "Game Over"
				print
				inRoom = "none"
				hasEscaped = -1
			else:
				print "You travel to a dusty room." 
				print "There is a note on the floor." 
  
				print 
				print "1) Main Room" 
				print "2) Pick up Note" 
				print 
  
				action = raw_input("choose #1-2: ") 
				action = int(action) 
  
				if action == 1: 
					inRoom = "main" 
				if action == 2: 
					print "The note says, '9278'"
					inRoom = "main" 
		else: 
			print
			print "The twin answered the left one."
			
			print
			print "1) left door"
			print "2) right door"
			print
			
			whichDoor = raw_input("Which door should you enter?   ")
			whichDoor = int(whichDoor)
			
			if whichDoor == 1:
				print
				print "You enter a long corridor."
				print "You keep running to the end, but there is no end"
				print "You try running back, but you never get back to the door you used to enter"
				print "Game Over"
				print
			else:
				print
				print "You travel to a dusty room." 
				print "There is a note on the floor." 
  
				print 
				print "1) Main Room" 
				print "2) Pick up note" 
				print 
  
				action2 = raw_input("choose #1-2: ") 
				action2 = int(action2)
				
				if action2 == 1: 
					inRoom = "main" 
				if action2 == 2: 			
					print "The note says, '9278'"
					inRoom = "main"
					
	if inRoom == "east":
		print
		print "You are stuck in an upside down room."
		print "There is a big red button"
		print
		print "1) Main Room" 
		print "2) Press red button"
		print
  
		action = raw_input("choose #1-2:   ") 
		action = int(action) 
  
		if action == 1: 
			inRoom = "main"
		elif action == 2:
			print
			print "A person appeared."
			print 'He says, "right, left, left, right"'
			
	while inRoom == "north":
	
		if inRoom == "north": 
			print "There are two ways you can go."
			print "Which way do you go?"
		  
			print 
			print "1) Left" 
			print "2) Right"
			print "3) Back to Main Room"
			print
		  
			action = raw_input("choose #1-3:   ") 
			action = int(action) 
		  
			if action == 1: 
				direcOne = "left"
			elif action == 2:
				direcOne = "right"
			elif action == 3:
				inRoom = "main"
				
		if inRoom == "north": 
			print "There are two more ways you can go."
			print "Which way do you go?"
	  
			print 
			print "1) Left" 
			print "2) Right"
			print "3) Back to Main Room"
			print
	  
			action = raw_input("choose #1-3:   ") 
			action = int(action) 
	  
			if action == 1: 
				direcTwo = "left"
			elif action == 2:
				direcTwo = "right"
			elif action == 3:
				inRoom = "main"
			
		if inRoom == "north": 
			print "There are two more ways you can go."
			print "Which way do you go?"
		  
			print 
			print "1) Left" 
			print "2) Right"
			print "3) Back to Main Room"
			print
		  
			action = raw_input("choose #1-3:   ") 
			action = int(action) 
		  
			if action == 1: 
				direcThree = "left"
			elif action == 2:
				direcThree = "right"
			elif action == 3:
				inRoom = "main"
					
		if inRoom == "north": 
			print "There are two more ways you can go."
			print "Which way do you go?"
	  
			print 
			print "1) Left" 
			print "2) Right"
			print "3) Back to Main Room"
			print
	  
			action = raw_input("choose #1-3:   ") 
			action = int(action) 
	  
			if action == 1: 
				direcFour = "left"
			elif action == 2:
				direcFour = "right"
			elif action == 3:
				inRoom = "main"
		
		if inRoom == "north":		
			if direcOne == "right" and direcTwo == "left" and direcThree == "left" and direcFour == "right":
				print "You finished the maze. Congratulations!!!"
				print "You find a key on the floor."
				
				print 
				print "1)Pick up key"
				print "2)Go back to main room"
				print
				
				choose = raw_input("Choose 1-2:   ")
				choose = int(choose)
				if choose == 1:
					hasKey = 1
					print "You picked up the key."
					inRoom = "main"

				if choose == 2:
					inRoom = "main"
		  
	if inRoom == "south": 
		print "There is a locked door here." 
		print "You need a password and a key to unlock the door"
		
		print 
		print "1) Main Room" 
		print "2) Unlock door" 
		print 
  
		action = raw_input("choose #1-2: ") 
		action = int(action) 
  
		if action == 1: 
			inRoom = "main" 
		if action == 2: 
			if hasKey == 1: 
				is_password = raw_input("What is the password?   ")
				if is_password == '9278':
					print "You have found the exit!" 
					print 'You win!' 
					print 'You won! Hurray \(^.^)/'
					hasEscaped = 1 
				else:
					print "That is the wrong password."
			else: 
				print "You need a key for that!" 
  

	
	if inRoom == "main": 
		print "You are in a scary warehouse." 
		print "Try to escape if you can!" 
  
		print 
		print "1) Move North" 
		print "2) Move South" 
		print "3) Move West" 
		print "4) Move East" 
		print 
  
		action = raw_input("choose #1-4: ") 
		action = int(action) 
  
		if action == 1: 
			inRoom = "north" 
		if action == 2: 
			inRoom = "south" 
		if action == 3: 
			inRoom = "west" 
		if action == 4: 
			inRoom = "east" 
			
