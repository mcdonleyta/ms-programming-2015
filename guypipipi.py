inRoom = "Main Room"
hasRainbowCottonCandy = 0
hasEscaped = 0
hasPotato = 0
hasAutomatic = 0

while hasRainbowCottonCandy == 0:
	if inRoom == "Main":
		print "You're in a bright purple room"
		
		print "1) Main Room" 
		print "2) Pick up Rainbow Cotton Candy"
		print "3) Dance Around"
	
		action = raw_input ("choose #1-3: ")
		action = int(action)
		
		if action == 1: 
		 inRoom = "Main"
		if action == 2:
			hasRainbowCottonCandy = 1
			if action == 3:
				print "You fell and died."
				
				
				
				
			
			
			 
		

