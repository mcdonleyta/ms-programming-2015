inRoom = "Main"
hasRainbowCottonCandy = 0
hasEscaped = 0
hasPotato = 0
hasAutomatic = 0
isAlive = 1

while hasRainbowCottonCandy == 0 and isAlive == 1:
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
			hasRainbowCottonCandy = 0
			print "Good job you won!"
			hasEscaped = 1 
			break 
		if action == 3:
			print "You fell through the floor and died!"
			isAlive = 0
			
				
			
				
			
	
				
				
				
				
				
				
			
			
			 
		
