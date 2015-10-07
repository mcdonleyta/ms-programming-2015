inRoom = "main"
hasKey = 0
hasEscaped = 0

while hasEscaped == 0:
	if inRoom == "Mid Lane":
		print "You stand facing a shadow he says No technique is forbidden. I am Zed the master of shadows"
		if hasKey == 0:
			print "You can choose to fight or run"
		
			print
			print "1) Fight"
			print "2) Run"
			print 
			
			action = raw_input("choose #1-2: ")
			action = int(action)
			
			if action == 1:
				inRoom = "Mid lane"
			if action == 2:
				inRoom = "Bot Lane"
				print "You have ran to bot lane" 
			
			action = raw_input("choose #1-2: ")
			action = int(action)
			
			if action == 1:
				inRoom = "Main"
			
			
	if inRoom == "Bot lane":
		print "You find two enemies Vayne and Leona, Vayne (The Night Hunter) is not tanky/defensive but is very very powerful, Leona (The Radiant Dawn) is very very tanky/defensive but she is not very powerful in attacking."
	
		print
		print "1) Main Room"
		print
		
		action = raw_input("choose #1: ")
		action = int(action)
		
		if action == 1:
			inRoom = "main"

	if inRoom == "north":
		print "It looks like this used to be a kitchen."
	
		print
		print "1) Main Room"
		print
		
		action = raw_input("choose #1: ")
		action = int(action)
		
		if action == 1:
			inRoom = "main"
	
	if inRoom == "south":
		print "There is a locked door here."
	
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
				print "You have found the exit!"
				print "You win!"
				hasEscaped = 1
			else:
				print "You need a key for that!"
	
	if inRoom == "main":
		print "You are in Summoners Rift."
		print "Go and try to destroy the enemy Nexus!"
		
		print
		print "1) Go to Top lane"
		print "2) Go to Jungle"
		print "3) Go to Mid lane"
		print "4) Go to Bot lane"
		print 
		
		action = raw_input("choose #1-4: ")
		action = int(action)
		
		if action == 1:
			inRoom = "Top"
		if action == 2:
			inRoom = "south"
		if action == 3:
			inRoom = "west"
		if action == 4:
			inRoom = "east"

print "You won! Hurray \(^.^)/"
