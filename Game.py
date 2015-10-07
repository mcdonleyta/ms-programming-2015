inFloor = "First"
hasGun = 0
hasSurvived = 0

while hasSurvived == 0:
	if inFloor == "First":
		print "You are in a zombie apocalypse. Sorry bout your luck! Anyways find the gun. After that, kill the zombie\n."
		print "1. Go up to second floor"
		print "2. Go up to third floor"
		print "3. Go up to fourth floor"
		

		action = raw_input("#Choose 1-4: ")
		action = int(action)

		if action == 1:
			inFloor = "Second Floor"
		if action == 2:
			inFloor = "Third Floor"
		if action == 3:
			inFloor = "Fourth Floor"
		
		
	if inFloor == "Second Floor":
		print "You find a dirty room with lots of plants."
		print "There is a table with a drawer."
		
		print "1.Open drawer."
		print "2. Leave floor"
		
		action = raw_input ("#Choose 1-2: ")
		action = int(action)
		
		if action == 1:
			openDrawer = 1
		if action == 2:
			leaveFloor = 2
			
	if inFloor == "Third Floor":
		print "The room was probably a bathroom."
		print "There is still a toilet"
		print "Gross"
		
		action= raw_input ("Choose #1: ")
		action = int(action)
				
		if action ==1:
			inFloor ="First floor"
				
	if inFloor == "Fourth Floor" :
		print "There is a back door to the outside"
		print "There is a weird noise in front of the door."
		print "There is a zombie!"
		print "1. Shoot zombie"
	
		
		action= raw_input ("Choose #1")
		action = int(action)
		
		
			if action ==1:
				print "You shot the zombie in the leg."
				print "1. shoot again"
				print
		
			action= raw_input ("Choose #1")
			action = int(action)
		 
		
			if action ==1:
				print "You have killed the zombie!"
				print "Tou win! The house if yours."
								
				action = raw_input ("Choose #1:")
				action = int(action)
		
				
				
			
			
				 
			
