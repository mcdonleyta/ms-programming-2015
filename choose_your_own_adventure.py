inRoom = "main"#9278
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
					print "The note says, '92__'"
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
					print			
					print "The note says, '92__'"
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
			print "A troll appeared."
			print 'He says, "I am a troll."'
			print '"I will ask you five questions"'
			print
			print '"Question 1: What do bees use to make honey?"'
			print "a) pollen"
			print "b) flower petals"
			print "c) nectar"
			print "d) shoe soles"
			print
			
			answer1 = raw_input("Type the letter of the correct answer:  ")
			
			if answer1 == "a":
				print
				print '"Wrong"'
				print
				print "The troll magically turned the room right-side up"
				print "He made the ceiling vanish and you fell out of the world"
				print
				print "Game Over"
				inRoom = "none"
				
			if answer1 == "b":
				print
				print '"Wrong"'
				print
				print "The troll magically turned the room right-side up"
				print "He made the ceiling vanish and you fell out of the world"
				print
				print "Game Over"
				inRoom = "none"
				
			if answer1 == "d":
				print
				print '"Wrong"'
				print
				print "The troll magically turned the room right-side up"
				print "He made the ceiling vanish and you fell out of the world"
				print
				print "Game Over"
				inRoom = "none"
				
			if answer1 == "c":
				print
				print '"Correct"'
				print
				
				print '"Question 2: What is the name of the fifth planet from the sun?"'
				print "a) Jupiter"
				print "b) Mars"
				print "c) Earth"
				print "d) Saturn"
				print
				
				answer2 = raw_input("Type the letter of the correct answer")
					
				if answer2 == "b":
					print
					print '"Wrong"'
					print
					print "The troll magically turned the room right-side up"
					print "He made the ceiling vanish and you fell out of the world"
					print
					print "Game Over"
					inRoom = "none"
					
				if answer2 == "d":
					print
					print '"Wrong"'
					print
					print "The troll magically turned the room right-side up"
					print "He made the ceiling vanish and you fell out of the world"
					print
					print "Game Over"
					inRoom = "none"
					
				if answer2 == "c":
					print
					print '"Wrong"'
					print
					print "The troll magically turned the room right-side up"
					print "He made the ceiling vanish and you fell out of the world"
					print
					print "Game Over"
					inRoom = "none"
					
				if answer2 == "a":
					print
					print '"Correct"'
					print
					print '"Question 3: What is the name of Cheetos\' mascot?"'
					print "a) Cheesy"
					print "b) Chester"
					print "c) Cheeser"
					print "d) Chessy"
					print
					
					answer3 = raw_input("Type the letter of the correct answer")
						
					if answer3 == "d":
						print
						print '"Wrong"'
						print
						print "The troll magically turned the room right-side up"
						print "He made the ceiling vanish and you fell out of the world"
						print
						print "Game Over"
						inRoom = "none"
						
					if answer3 == "c":
						print
						print '"Wrong"'
						print
						print "The troll magically turned the room right-side up"
						print "He made the ceiling vanish and you fell out of the world"
						print
						print "Game Over"
						inRoom = "none"
						
					if answer3 == "a":
						print
						print '"Wrong"'
						print
						print "The troll magically turned the room right-side up"
						print "He made the ceiling vanish and you fell out of the world"
						print
						print "Game Over"
						inRoom = "none"
						
					if answer3 == "b":
						print
						print '"Correct"'
						print
						print '"Question 4: Poor people have it. Rich people need it. If you eat it you die."'
						print
					
						answer4 = raw_input('"What is it?"')
						
						if answer4 != "Nothing":
							print
							print '"Wrong"'
							print
							print "The troll magically turned the room right-side up."
							print "He made the ceiling vanish and you fell out of the world."
							print
							print "Game Over"
							inRoom = "none"
							
						else:
							print
							print '"Correct"'
							print
							print '"Question 5: I occur twice in a week, once in a year but never in a day."'
							print 
							
							answer5 = raw_input("What am I?")
							
							if answer5 != "The Letter E":
								print
								print '"Wrong"'
								print
								print "The troll magically turned the room right-side up."
								print "He made the ceiling vanish and you fell out of the world."
								print
								print "Game Over"
								inRoom = "none"
							else:
								print
								print '"Correct"'
								print
								print '"You answered all the questions right!"'
								print "The troll gave you a piece of paper"
								print "It says, 'Right, Left, Left, Right'"
								print
								
								inRoom = "main"
								
								
	while inRoom == "north":
	
		if inRoom == "north": 
			print
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
			print 
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
			print
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
			print
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
				print
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
		print 
		print "There is a locked door here." 
		print "You need a password and a key to unlock the door"
		print "There is another door to the right."
		
		print 
		print "1) Main Room" 
		print "2) Unlock door" 
		print "3) Go to the door on the right."
		print 
  
		action = raw_input("choose #1-3: ") 
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
					print
					print "That is the wrong password."
					print
			else:
				print 
				print "You need a key for that!" 
				print
		if action == 3:
			print
			print "There is a bomb." 
			fastPress = raw_input("Press the 7 key FAST to deactivate the bomb!!! ")
			fastPress = str(fastPress)
			
			if fastPress != "7":
				print
				print "You pressed the wrong key"
				print 100 * "BOOM BAM! BOW!"
				print "Game Over"
				inRoom = "none"
			else:
				print 
				print "You deactivated the bomb!"
				print
				print "You travel to a slimy room."
				print "There is a note on the floor."
				print
				print "1) Pick up note"
				print "2) Back to Main Room"
				print
				
				action3 = raw_input("Choose #1-2:   ")
				action3 = int(action3)
				
				if action3 == 1:
					print
					print "The note says __78"
				else:
					inRoom = "main"
					
	if inRoom == "main":
		print 
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
			
	
