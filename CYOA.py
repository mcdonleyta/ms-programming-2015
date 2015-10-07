inRoom = "main"
hasKey = 0
hasEscaped = 0
dead = 0
gun = 0
men_dead = 0
trapdoor = 0
beenInMain = 0
beenInWest = 0
beenInEast = 0
while hasEscaped == 0 and dead == 0:
	
	if inRoom == "west":
	
		if beenInWest == 0:
			print "You travel to a dusty room."
			print "There is a key on the floor."
		
			print
			print "1) Main Room"
			print "2) Pick up Key"
			print
			
			action = raw_input("choose #1-2: ")
			action = int(action)
			
			if action == 1:
				inRoom = "main"
				beenInWest = 1
			if action == 2:
				hasKey = 1
				beenInWest = 1

		if beenInWest == 1:
			print "You come back into the dusty room."
		
			print "1) Main Room"
			if haskey == 0:
				print "2) Pick up Key"
			
			action = raw_input("choose #1-2: ")
			action = int(action)
			
			if action == 1:
				inRoom = "main"
			if action == 2:
				hasKey = 1

	if inRoom == "east":
		if beenInEast == 0:
			print "You find a small bedroom long abandoned."
			print "You see a door."
		
			print "1) Main Room"
			print "2) Try door"
			
			action = raw_input("choose #1-2: ")
			action = int(action)

			if action == 1:
				inRoom = "main"
				beenInEast = 1
			if action == 2:
				inRoom = "secret 1"
				beenInEast = 1
			
			if beenInEast == 1:
				print "You come back int the bedroom."
				print "You see a door."
			
				print "1) Main Room"
				print "2) open door"
				
				action = raw_input("choose #1-2: ")
				action = int(action)

				if action == 1:
					inRoom = "main"
				if action == 2:
					inRoom = "secret 1"
			
	if inRoom == "secret 1":
		print "You enter a clean room with other people in it"
		print "They are staring at you" 
		
		if gun == 0:
			print "1) start talking"
			print "2) go back to the east room"
			print "3) Walk towards them."
			
			action = raw_input("choose #1-3: ")
			action = int(action)
			
			if action == 1:
				dead = 1
			if action == 2:
				inRoom = "east"
			if action == 3:
				dead = 1
				
		if gun == 1:
			print "1) go back to the east room"
			print "2) start talking"
			print "3) Walk towards them."
			print "4) shoot them"
			
			action = raw_input("choose #1-4: ")
			action = int(action)
			
			if action == 1:
				inRoom = "east"
			if action == 2:
				dead = 1
			if action == 3:
				dead = 1
			if action == 4:
				print "they died"
				men_dead = 1
			

	if inRoom == "north":
		print "It looks like this used to be a kitchen."
		print "There is cabinets lineing the walls"
		if gun == 0:
			print "1) Main Room"
			print "2) open the cabinets"
		
		action = raw_input("choose #1-2: ")
		action = int(action)
		
		if action == 1:
			inRoom = "main"
		if action == 2:
			gun = 1
			print "you found a gun"
		if gun == 1:
				print "1) main room"
				print "2) explore the room"
		
		action = raw_input("choose #1-2: ")
		action = int(action)
			
		if action == 1:
			inRoom = "main"
		if action == 2:
			print "you found a trapdoor"
			trapdoor = 1
			print "1) enter trapdoor"
			print "2) leave room"
		
			
	
	if inRoom == secret_2:
		print "you enter a dark room with now windows and only one bare lightbulb"
		
		print "1) leave the room"
		print "2) explore the room"
		
			
		action = raw_input("choose #1-2: ")
		action = int(action)
			
		if action == 1:
			inRoom = "north"
		if action == 2:
			print "you found a old loaf of bread"
			
			print "1) leave room"
			
			action = raw_input("choose #1: ")
			action = int(action)
			
		if action == 1:
			inRoom = "north"
		
	if inRoom == "south":
		print "There is a locked door here."
	
		print "1) Main Room"
		print "2) Unlock door"
		
		action = raw_input("choose #1-2: ")
		action = int(action)
		
		if action == 1:
			inRoom = "main"
		if action == 2:
			if hasKey == 1:
				print "You have found the exit!"
				print "You win!"
				hasEscaped = 1
			else:
				print "You need a key for that!"
	
	if beenInMain == 0:
		if inRoom == "main":
			print "You are in a scary warehouse."
			print "Try to escape if you can!"
			print "if you don't get out, you die"
			
			
			print "1) Move North"
			print "2) Move South"
			print "3) Move West"
			print "4) Move East"
			
			action = raw_input("choose #1-4: ")
			action = int(action)
			
			if action == 1:
				inRoom = "north"
				beenInMain = 1
			if action == 2:
				inRoom = "south"
				beenInMain = 1
			if action == 3:
				inRoom = "west"
				beenInMain = 1
			if action == 4:
				inRoom = "east"
				beenInMain = 1
			
	if beenInMain == 1:
		print "you are back in the main room"
			
		print "1) Move North"
		print "2) Move South"
		print "3) Move West"
		print "4) Move East"
		print "5) Explore the room"
		
		action = raw_input("choose #1-5: ")
		action = int(action)
		
		if action == 1:
			inRoom = "north"
		if action == 2:
			inRoom = "south"
		if action == 3:
			inRoom = "west"
		if action == 4:
			inRoom = "east"
		if action == 5:
			
		
	
		if dead != 0
			print "you died"
		else: 
			print "You won! Hurray \(^.^)/"
