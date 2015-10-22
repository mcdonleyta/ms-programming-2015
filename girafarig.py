<<<<<<< HEAD
#max adventure game

=======
>>>>>>> 3fc16bb5d98d8304c4b4b2c0960448734551cedb
inRoom = "main"
haskey = 0
hasAutomatic = 0
hasKnife = 0
hasFrag = 0
hasSword = 0
hasPistol = 0
hasRocketlauncher = 0
hasEscaped = 0
isAlive = 1
print "You are stuck in a large building, you better try to escape!"

while hasEscaped == 0 and isAlive == 1:
	if inRoom == "main":
		 print "There are four rooms which one do you want to go into"
		 
		 print "First Room"
		 print "Second Room"
		 print "Third Room"
		 print "Fourth Room"
		 
		 action = raw_input("Choose #1:4.")
		 
		 if action == "first room" or action == "1" or action == "first":
			inRoom = "North"
		 if action == "second room" or action == "2"  or action == "second":
			inRoom = "South"
		 if action == "third room" or action == "3" or action == "third":
			 inRoom = "West"
		 if action == "fourth room" or action == "4" or action == "fourth":
			 inRoom = "East"
			 
	if inRoom == "North":
			print "This room seems pretty empty except for the knife"
			
			print "1) pick up knife"
			print "2) turn back"
			print "3) fight him"	
			action = raw_input("Choose 1,2 or 3")
	
			if action == "pick up knife" or action == "1":
				print " An Addy appeared, and a knife can't stop him!"
				isAlive = 0
			if action == "turn back" or action == "2":
				inRoom = "main"
			if action == "fight him" or action == "3" or action == "fight":
				if hasAutomatic == 1 or hasPistol == 1 or hasRocketlauncher == 1:
					print "those weapons were strong enough to stop him you survived"
				else:
					print "you couldn't stop him"
					isAlive = 0
	if inRoom == "South":
		print "This room has a lot of weapons laying around"
		
<<<<<<< HEAD
		print "Only pick one of them and then return to the main room"
		
=======
>>>>>>> 3fc16bb5d98d8304c4b4b2c0960448734551cedb
		print "1) pick up automatic"
		print "2) pick up knife"
		print "3) pick up sword"
		print "4) pick up pistol"
		print "5) go back to main room"
		
		weapon = raw_input("choose a weapon or turn back")

		if weapon == "1" or weapon == "pick up automatic" or weapon == "automatic":
			print "you got the automatic"
			hasAutomatic = 1
		if weapon == "2" or weapon == "pick up knife" or weapon == "knife":
			print "you got the knife"
			hasKnife = 1	
		if weapon == "3" or weapon == "pick up sword" or weapon == "sword":
			print "you got the sword"
			hasSword = 1
		if weapon == "4" or weapon == "pick up pistol" or weapon == "pistol":
			print "you got the pistol"
			hasPistol = 1
		if weapon == "5" or weapon == "go back to main room" or weapon == "main room":
			inRoom = "main"

	if inRoom == "West":
		print "OMG ZOMBIES!"
		
		print "1) coward back to main room"
		print "2) fight them"
		
		fight = raw_input("what do you want to do")
	
<<<<<<< HEAD
		if fight  == "coward away" or fight == "go back to main room" or fight == "main room" or fight == "1":
			inRoom = "main"

		if fight == "fight them" or fight == "fight" or fight == "2":
			if hasSword == 1 or hasKnife ==1 or hasFrag == 1 or hasRocketlauncher == 1:
				print "You were able to finish off all of them YOU WIN cuz you didn't have to reload!"
				hasEscaped = 1
			elif hasAutomatic == 1 or hasPistol == 1:
				print "you lose you were a little dumb guy cuz why u were reloading u died"
				isAlive = 0
=======
		if fight  == "coward away" or fight == "go back to main room" or fight == "main room" or fight == "2":
			inRoom = "main"

			if fight == "fight them" or fight == "fight" or fight == "2":
				if hasSword == 1 or hasKnife ==1 or hasFrag == 1 or hasRocketlauncher == 1:
					print "You were able to finish off all of them you win!"
					hasEscaped = 1
				else:
					print "you lose you were a little dumb guy"
					isAlive = 0
>>>>>>> 3fc16bb5d98d8304c4b4b2c0960448734551cedb



	if inRoom == "East":
		print "this room has 3 things"
		
<<<<<<< HEAD
		print "Only take one then return to the main room"
		
=======
>>>>>>> 3fc16bb5d98d8304c4b4b2c0960448734551cedb
		print "1) rocket launcher"
		print "2) frag"
		print "3) tank"
		print "4) turn back"
		
		action = raw_input("Choose something to do")
		
		if action == "1" or action == "rocket launcher":
			print "you got the rocket launcher"
			hasRocketlauncher = 1
		if action == "2" or action == "frag":
			print "you got the Frag"
			hasFrag = 1
		if action == "3" or action == "tank":
			print "it was rigged with explosives you died"
			isAlive = 0
		if action == "4" or action == "main room" or action == "main":
			inRoom = "main"
		
		
		








<<<<<<< HEAD
=======























































>>>>>>> 3fc16bb5d98d8304c4b4b2c0960448734551cedb
